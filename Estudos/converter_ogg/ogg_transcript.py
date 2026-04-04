#!/usr/bin/env python3
"""
ogg2txt.py — Transcreve áudios .ogg para .txt

Modos de uso:
1) Local (rápido e offline) com Faster-Whisper  →  --engine local
   - Requer: pip install faster-whisper ffmpeg-python
   - Requer ffmpeg instalado no sistema (ffmpeg -version)

2) OpenAI Whisper API (nuvem) → --engine openai
   - Requer: pip install openai
   - Requer variável de ambiente OPENAI_API_KEY

Exemplos:
  python ogg2txt.py input.ogg
  python ogg2txt.py input.ogg -o saida.txt
  python ogg2txt.py input.ogg --engine local --model small --language pt
  python ogg2txt.py input.ogg --engine openai -o saida.txt

Saída: um arquivo .txt com a transcrição.
"""
import argparse
import os
import sys
import tempfile
from pathlib import Path
import subprocess


""" 
e você não precisa de GPU (ou seja, só quer usar CPU)
"""
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

def ensure_ffmpeg():
    ffmpeg_dir = os.path.join(os.getcwd(), "ffmpeg-2025-10-09-git-469aad3897-full_build", "bin")
    os.environ["PATH"] += os.pathsep + ffmpeg_dir

    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False

def convert_to_wav(input_path: Path) -> Path:
    """
    Converte qualquer áudio suportado pelo ffmpeg para WAV mono 16kHz.
    Retorna o caminho do WAV temporário.
    """
    if not ensure_ffmpeg():
        print("ERRO: ffmpeg não encontrado. Instale-o e garanta que 'ffmpeg' esteja no PATH.", file=sys.stderr)
        sys.exit(1)
    tmp_wav = Path(tempfile.mkstemp(suffix=".wav")[1])
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-ac", "1",           # mono
        "-ar", "16000",       # 16 kHz
        "-f", "wav",
        str(tmp_wav)
    ]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        print("ERRO na conversão com ffmpeg:", r.stderr.decode(errors="ignore"), file=sys.stderr)
        sys.exit(1)
    return tmp_wav

def transcribe_local(wav_path: Path, model_name: str, language: str, beam_size: int = 5) -> str:
    """
    Transcreve com Faster-Whisper localmente (CPU).
    """
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERRO: 'faster-whisper' não está instalado. Rode: pip install faster-whisper", file=sys.stderr)
        sys.exit(1)

    # Força uso da CPU e evita float16 (que exige GPU/CUDA)
    compute_type = "float32"
    device = "cpu"
    model = WhisperModel(model_name, device=device, compute_type=compute_type)

    segments, info = model.transcribe(str(wav_path), language=language or None, beam_size=beam_size)
    text_parts = [seg.text.strip() for seg in segments]
    return " ".join([t for t in text_parts if t])


def transcribe_openai(input_path: Path, language: str) -> str:
    """
    Transcreve usando a API Whisper da OpenAI.
    - Requer OPENAI_API_KEY no ambiente.
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("ERRO: 'openai' não está instalado. Rode: pip install openai", file=sys.stderr)
        sys.exit(1)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERRO: variável de ambiente OPENAI_API_KEY não definida.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    # Envia o arquivo original (ogg) — a API aceita vários formatos
    with open(input_path, "rb") as f:
        # Modelo de transcrição padrão
        resp = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language or None,
            temperature=0.0
        )
    # resp.text (SDK v1) retorna a transcrição
    return resp.text.strip() if hasattr(resp, "text") else str(resp)

def main():
    parser = argparse.ArgumentParser(description="Transcreve arquivos .ogg em texto (.txt)")
    parser.add_argument("input", type=Path, help="Caminho do arquivo .ogg (ou outro formato de áudio suportado)")
    parser.add_argument("-o", "--output", type=Path, help="Arquivo de saída .txt (default: mesmo nome do input)")
    parser.add_argument("--engine", choices=["local", "openai"], default="local", help="Motor de transcrição (padrão: local)")
    parser.add_argument("--model", default="base", help="Modelo do Faster-Whisper (tiny, base, small, medium, large, etc.)")
    parser.add_argument("--language", default="pt", help="Idioma principal do áudio (ex: pt, en, es). Para detectar automaticamente, deixe vazio ('').")
    parser.add_argument("--beam", type=int, default=5, help="Beam size (local). Valores maiores podem melhorar qualidade, mas ficam mais lentos.")
    args = parser.parse_args()

    input_path = args.input
    if not input_path.exists():
        print(f"ERRO: arquivo não encontrado: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Define saída
    if args.output:
        out_txt = args.output
    else:
        out_txt = input_path.with_suffix(".txt")

    try:
        if args.engine == "local":
            # Converte para WAV padronizado para melhor estabilidade
            wav_path = convert_to_wav(input_path)
            try:
                text = transcribe_local(wav_path, model_name=args.model, language=(args.language or None), beam_size=args.beam)
            finally:
                # Remove temporário
                try:
                    os.remove(wav_path)
                except Exception:
                    pass
        else:
            text = transcribe_openai(input_path, language=args.language or None)

        # Grava saída
        out_txt.parent.mkdir(parents=True, exist_ok=True)
        out_txt.write_text(text + "\n", encoding="utf-8")
        print(f"OK: transcrição salva em: {out_txt}")
    except KeyboardInterrupt:
        print("\nCancelado pelo usuário.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print("ERRO inesperado:", str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

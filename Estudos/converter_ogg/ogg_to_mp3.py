import argparse
import os
import sys
import tempfile
from pathlib import Path
import subprocess


def ensure_ffmpeg():
    ffmpeg_dir = os.path.join(os.getcwd(), "ffmpeg-2025-10-09-git-469aad3897-full_build", "bin")
    os.environ["PATH"] += os.pathsep + ffmpeg_dir
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False


def convert_to_wav(input_path: Path) -> Path:
    """Converte qualquer áudio suportado pelo ffmpeg para WAV mono 16kHz."""
    if not ensure_ffmpeg():
        print("ERRO: ffmpeg não encontrado. Instale-o e garanta que 'ffmpeg' está no PATH.", file=sys.stderr)
        sys.exit(1)

    tmp_wav = Path(tempfile.mkstemp(suffix=".wav")[1])
    cmd = ["ffmpeg", "-y", "-i", str(input_path), "-ac", "1", "-ar", "16000", "-f", "wav", str(tmp_wav)]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        print("ERRO na conversão com ffmpeg:", r.stderr.decode(errors="ignore"), file=sys.stderr)
        sys.exit(1)
    return tmp_wav


def convert_to_mp3(input_path: Path) -> Path:
    """Converte qualquer áudio suportado pelo ffmpeg para MP3 (128 kbps)."""
    if not ensure_ffmpeg():
        print("ERRO: ffmpeg não encontrado. Instale-o e garanta que 'ffmpeg' está no PATH.", file=sys.stderr)
        sys.exit(1)

    mp3_path = input_path.with_suffix(".mp3")
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-vn",
        "-ar", "44100",
        "-b:a", "128k",
        "-f", "mp3",
        str(mp3_path)
    ]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        print("ERRO na conversão com ffmpeg:", r.stderr.decode(errors="ignore"), file=sys.stderr)
        sys.exit(1)
    return mp3_path


def transcribe_local(wav_path: Path, model_name: str, language: str, beam_size: int = 5) -> str:
    """Transcreve com Faster-Whisper localmente (CPU)."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERRO: 'faster-whisper' não está instalado. Rode: pip install faster-whisper", file=sys.stderr)
        sys.exit(1)

    compute_type = "float32"
    device = "cpu"
    model = WhisperModel(model_name, device=device, compute_type=compute_type)

    segments, info = model.transcribe(str(wav_path), language=language or None, beam_size=beam_size)
    text_parts = [seg.text.strip() for seg in segments]
    return " ".join([t for t in text_parts if t])


def transcribe_openai(input_path: Path, language: str) -> str:
    """Transcreve usando a API Whisper da OpenAI."""
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
    with open(input_path, "rb") as f:
        resp = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language or None,
            temperature=0.0
        )
    return resp.text.strip() if hasattr(resp, "text") else str(resp)


def main():
    parser = argparse.ArgumentParser(description="Transcreve arquivos .ogg em texto (.txt) e pode converter para MP3.")
    parser.add_argument("input", type=Path, help="Caminho do arquivo de áudio (.ogg, .mp3, etc.)")
    parser.add_argument("-o", "--output", type=Path, help="Arquivo de saída .txt")
    parser.add_argument("--engine", choices=["local", "openai"], default="local", help="Motor de transcrição")
    parser.add_argument("--model", default="base", help="Modelo do Faster-Whisper (tiny, base, small, medium, large)")
    parser.add_argument("--language", default="pt", help="Idioma (ex: pt, en, es)")
    parser.add_argument("--beam", type=int, default=5, help="Beam size (local).")
    parser.add_argument("--to-mp3", action="store_true", help="Converte o arquivo de entrada para MP3.")
    args = parser.parse_args()

    input_path = args.input
    if not input_path.exists():
        print(f"ERRO: arquivo não encontrado: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Conversão opcional para MP3
    if args.to_mp3:
        mp3_path = convert_to_mp3(input_path)
        print(f"✅ MP3 gerado em: {mp3_path}")

    # Saída padrão .txt
    out_txt = args.output or input_path.with_suffix(".txt")

    try:
        if args.engine == "local":
            wav_path = convert_to_wav(input_path)
            try:
                text = transcribe_local(wav_path, model_name=args.model, language=(args.language or None), beam_size=args.beam)
            finally:
                try:
                    os.remove(wav_path)
                except Exception:
                    pass
        else:
            text = transcribe_openai(input_path, language=args.language or None)

        out_txt.parent.mkdir(parents=True, exist_ok=True)
        out_txt.write_text(text + "\n", encoding="utf-8")
        print(f"✅ Transcrição salva em: {out_txt}")
    except KeyboardInterrupt:
        print("\nCancelado pelo usuário.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print("ERRO inesperado:", str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


    """ 
     
      # Converter para MP3
python main.py meu_audio.ogg --to-mp3

# Transcrever localmente
python main.py meu_audio.ogg --engine local --model small --language pt

# Transcrever via API da OpenAI
python main.py meu_audio.ogg --engine openai -o saida.txt

# Converter e transcrever
python main.py meu_audio.ogg --to-mp3 --engine local

        """
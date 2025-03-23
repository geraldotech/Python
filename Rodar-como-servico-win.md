# Rodar como um serviço no Windows e portabilizar


Para que o aplicativo rode como um serviço no Windows, você pode usar o NSSM (Non-Sucking Service Manager), que é uma ferramenta simples para gerenciar serviços no Windows.

Passos:

Baixe o NSSM: https://nssm.cc/download

Extraia o executável do NSSM.

Abra o terminal (cmd) como administrador e execute:

nssm install MeuServicoPython

No NSSM:

No campo Path, selecione o executável do Python (geralmente python.exe ou pythonw.exe).

No campo Startup directory, selecione a pasta onde está o seu script Python.

No campo Arguments, coloque o nome do seu script (ex: servico.py).

Clique em Install service.

Agora, seu aplicativo Python rodará como um serviço no Windows.


# Empacotamento (Opcional) - portabilizar
Se quiser distribuir seu aplicativo, você pode empacotá-lo usando ferramentas como PyInstaller ou cx_Freeze para criar um executável.

Exemplo com PyInstaller:

pip install pyinstaller
pyinstaller --onefile servico.py
Isso criará um arquivo .exe que pode ser executado diretamente no Windows.


Para que o PyInstaller inclua arquivos externos, como o config.json, no executável gerado, você precisa especificar esses arquivos durante o processo de empacotamento. O PyInstaller não inclui automaticamente arquivos que não são .py, então você precisa usar o parâmetro --add-data para garantir que o config.json (e outros arquivos necessários) sejam embutidos no executável.

pyinstaller --onefile --add-data "config.json;." start.py


mover o executavel para uma pasta e suas dependencias e executar o exe


- Criando batch que cria o serviço silenciosamente

```shell
@echo off
REM Script para instalar e configurar o serviço "a_agendador" usando o NSSM

REM Defina o caminho para o nssm.exe
set NSSM_PATH=%SCRIPT_DIR%nssm.exe

REM Defina o nome do serviço
set SERVICE_NAME=a_agendador_v2

REM Obter o diretório atual onde o script está sendo executado
set SCRIPT_DIR=%~dp0

REM Definir o caminho para o executável (assumindo que está na mesma pasta do script)
set APP_PATH=%SCRIPT_DIR%start_timer.exe

REM Defina o diretório de trabalho (usando o mesmo diretório do script)
set WORK_DIR=%SCRIPT_DIR%

REM Instalar o serviço
%NSSM_PATH% install %SERVICE_NAME% %APP_PATH%

REM Configurar o nome de exibição do serviço
%NSSM_PATH% set %SERVICE_NAME% DisplayName "Agendador de Tarefas 2"

REM Configurar a descrição do serviço
%NSSM_PATH% set %SERVICE_NAME% Description "Serviço para agendar tarefas com base em um arquivo config.json."

REM Configurar o diretório de trabalho
%NSSM_PATH% set %SERVICE_NAME% AppDirectory %WORK_DIR%

REM Iniciar o serviço
%NSSM_PATH% start %SERVICE_NAME%

echo Serviço "%SERVICE_NAME%" instalado e iniciado com sucesso!
echo Executável: %APP_PATH%
echo Diretório de trabalho: %WORK_DIR%
pause
```
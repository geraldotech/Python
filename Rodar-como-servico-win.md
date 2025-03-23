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
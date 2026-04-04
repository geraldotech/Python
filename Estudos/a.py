import os
import time
import subprocess
file = "a.py" 
last_mtime = os.path.getmtime(file)


price = 50
gege = 'geraldo filho'

def converter(x):
    return x * 10

print(f"vamos dobrar 5 agora vale {converter(5)}")
print("website: {} ou {}".format(price, gege))
print(f'{"":=^50}')

print("estou aprendendo python, \n lets break some lines")

print("Geraldo Filho"*5)









while True:
    try:
        mtime = os.path.getmtime(file)
        # só executa se a modificação foi realmente depois da última execução
        if mtime > last_mtime:
            last_mtime = mtime
          #  print(f"\n🔄 Alteração detectada pelo usuário. Executando {file}...\n")
            subprocess.run(["python", file])
        time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Watcher encerrado.")
        break
    except FileNotFoundError:
        print(f"⚠ Arquivo {file} não encontrado. Aguardando ser criado...")
        time.sleep(1)



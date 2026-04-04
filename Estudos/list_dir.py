from datetime import datetime
import os

print(os.listdir('.'))  # Lista arquivos e pastas no diretório atual

print('getcwd', os.getcwd())

print(os.name)  # Exibe 'posix' (Linux/Mac) ou 'nt' (Windows)

# Path desejado
lerdownloads = r'C:\xampp\htdocs\sga\logs'

# Muda para o diretório especificado
os.chdir(lerdownloads)

print("Diretório atual =>", os.getcwd())

# Lista arquivos da pasta
arquivos = os.listdir()

print("Arquivos encontrados:")
for arquivo in arquivos:
    print(" -", arquivo)

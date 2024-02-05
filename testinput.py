file = "text.txt"
name = input("Qual seu nome ?")

with open(file, 'w',encoding='utf-8') as my_file:
    my_file.write(name.upper())

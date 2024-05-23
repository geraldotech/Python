# Python


<details>
  <summary>
    Install Windows
  </summary>
Python3 e o IDLE
  
- [https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)

- check version: `python --version`

- select option: **`Add Python to environment variables`**

Windows after install setup enviroment > path > click edit
![image](https://github.com/geraldotech/Python/assets/92253544/23880d06-e9b4-4d73-8ee0-166f50babcdc)

 add a new:

 ![image](https://github.com/geraldotech/Python/assets/92253544/4aa8cf35-9f88-4a81-9036-cce5a84feaeb)
  
</details>


run `python` in cmd:

Open cmd with : `C:\Users\username\AppData\Local\Programs\Python\Python311`

run files:
`C:\Users\username\AppData\Local\Programs\Python\Python311\python.exe myscript.py`

### Modo iterativo:

abrir o IDLE Shell e testar comando direto

### Modo script:

abrir o `**IDLE Shell File > New File > fazer o script >**` save and run F5

### Python extension for Visual Studio Code

[https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

```py
zen Python:
import this
```

### comments:

```py
# single

'''
How is today ?
multiple lines
'''

```

### Tipos Primitivos e Saída de Dados

- int | 7 -4 0 9875 `números inteiros`
  - n1 = int(input("n1"))
- float | 4.5 0.076 -15.223 7.0 `números reais`
- bool | True / False
- str "Hello" "7.5" ''

```py
x = str("geraldox.com")

print("website:", x)
print("website: " + x)
print("website: {}".format(x))

#usando aspas between strings
print('Handle \'Option 1\'') # Handle 'Option 1'
print("how is \"idade\"")

#adiciona 50 iguais =
print(f'{"":=^50}')

#with string
print(f'Upper, {name:=^20}'.upper())

#alinhamentos # Alinhamentos: https://youtu.be/Vw6gLypRKmY?t=1349

"""
> left
< right
^ center
"""
print(f"How is going: {a:^20} !") # How is going:       Geraldo        !

print("Hello"*5) # HelloHelloHelloHelloHello

# end parameter in print()
print("gmap", end="@")
print("server.com") #gmap@server.com

# contrabarraN
print("Estou apredendo Python, \n Lets break some limes")
"""
Estou apredendo Python,
 Lets break some limes
"""

#print five
print("Hello"*5) # print("Hello"*5)
```

### Save to file.txt

write

```py
file_name = 'example.txt'

f = open(file_name, 'w', encoding='utf-8')

f.write(input('Your message: '))

f.close()

```

with open

```py
file = "text.txt"
name = input("Qual seu nome ?")

with open(file, 'w',encoding='utf-8') as my_file:
    my_file.write(name)

```

upper()

```py
file = "text.txt"
name = input("Qual seu nome ?")

with open(file, 'w',encoding='utf-8') as my_file:
    my_file.write(name.upper())
```

Python docx:

`install python-docx` [read](https://python-docx.readthedocs.io/en/latest/user/install.html#install)

leitura de paragrafos

```jsx
for para in documento.paragraphs:
    print(para.text)
```

```jsx
word = 'Dictionary'
p = documento.add_paragraph()
runner = p.add_run(word)
runner.bold = True
runner.italic = True
```

for in obj

```jsx
referencias = {
   "xxxxxx": nf,
   "yyyyyyyy": vendacasada,
      "zzzz": origem,
  "kkkk": destino,
}

for attr, value in referencias.items():
        print(attr, value)
```

```jsx
print(referencias.pop('kkkk'))

dc = {k: v for k, v in referencias.items() if k.endswith('k')}
print(dc)
```

PDF:

> Microsoft Word (must be installed).
> `pip install docx2pdf` 9.02MB

bug:\***\*ModuleNotFoundError: No module named 'pywintypes' -solution\*\***
https://www.youtube.com/watch?v=ClGNW7_lxc4&ab_channel=Trinitysoftwareacademy

Go to: `C:\Users\gmap\AppData\Local\Programs\Python\Python311\Lib\site-packages\pywin32_system32` copy two dll files and Paste in `C:\Users\gmap\AppData\Local\Programs\Python\Python311\Lib`

py to exe:

```py
pip install auto-py-to-exe

auto-py-to-exe
```

REF: https://www.youtube.com/watch?v=Kp_41haOVQk&ab_channel=WalissonSilva

# format.()

> usando mask

```py
msn = str('O Blog do {0} is very good merece {1}')
txt = msn.format('Geraldo', 5)
print(txt)


nf = 2000
tes = ('set address {}.{}\n'.format('local', nf))
print(tes)


nome = input("Digite seu nome:")
print('prazer em te conhecer {}'.format(nome))


n1 = int(input("n1: "))
n2 = int(input("n2: "))
s = n1 + n2
print("A soma entre {} e {} = {}".format(n1, n2, s))
# se quiser pode adicionar a ordem, não obrigatórioÇ
print("A soma entre {0} e {1} = {2}".format(n1, n2, s))


# NEW version
nome = "Geraldo"
idade = 31
print(f'Como vai {nome} sua idade menos 10 seria {idade - 10}')

name = input('Enter a value: ')

print("Numerico: ",name.isnumeric())


# old
print("Value digitado: {}".format(name))
print("Alpha: {}".format(name).isalpha())

#adiciona 50 iguais =
print(f'{"":=^50}')

# new
print(f'Valor digitado {name.isalpha()}')
print(f"isCapitalize: {name.istitle()}")


```

- https://stackoverflow.com/questions/32240277/how-do-i-concat-strings-and-variables-in-a-file
- https://www.w3schools.com/python/python_string_formatting.asp

# Data Types

int, str, float

```py
number = int(input("Enter a positive number: "))

# convert str to int
opt = input("Digite um numero")
x = int(opt)
print(type(opt))
print(type(x))

# convert int to str
age = 32
str(age)
```

### Dictionary how run:

```py
mydicionario = {
    "X": msn
}

for k, v in mydicionario.items():
    print(k, v)
```

## Ordem de precedência:

- `()`
- `**`
- `* / // %` "multiplicação, divisão, divisão inteira, resto da divisão"

- potência pow(2,3) or 2\*\*3

### Links:

- https://bobbyhadz.com/blog/python-syntaxerror-invalid-syntax-pip-install

- https://bobbyhadz.com/blog/python-save-user-input-to-file

- https://stackoverflow.com/questions/57536995/how-to-change-font-size-of-all-docx-document-with-python-docx

- [AttributeError: 'str' object has no attribute 'X in Python | bobbyhadz](https://bobbyhadz.com/blog/python-attributeerror-str-object-has-no-attribute)

- [5. Data Structures — Python 3.11.4 documentation](https://docs.python.org/3/tutorial/datastructures.html)

- [How To Use Python-docx – vegibit](https://vegibit.com/how-to-use-python-docx/)

- [Change dictionary key in Python | note.nkmk.me](https://note.nkmk.me/en/python-dict-change-key/)

- [Remove an item from a dictionary in Python (clear, pop, popitem, del) | note.nkmk.me](https://note.nkmk.me/en/python-dict-clear-pop-popitem-del/)

- https://stackoverflow.com/questions/34779724/python-docx-replace-string-in-paragraph-while-keeping-style

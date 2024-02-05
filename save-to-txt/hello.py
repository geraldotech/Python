# ✅ Save user input to file
file_name = 'example2.txt'

with open(file_name, 'w', encoding='utf-8') as my_file:
    my_file.write(input('Your message: '))

# -------------------------------------------------

# ✅ Take filename and contents of file from user input

file_name = input('Filename with extension, e.g. example.txt: ')

with open(file_name, 'w', encoding='utf-8') as my_file:
    my_file.write(input('Your message: '))

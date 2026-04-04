import tkinter as tk

def get_name():
    name = entry.get()
    label.config(text=f"Olá {name}!")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Enviar", command=get_name)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()

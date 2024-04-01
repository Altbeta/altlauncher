from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import os
import string

name = "Altlauncher"
ver = 0.1

libraries = "client/minecraft.jar;client/jinput.jar;client/lwjgl_util.jar;client/lwjgl.jar;"
special_chars = ['@', "'", '"', '№', '#', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '{', '}', '[', ']', '|', '/', ',', '`', '~', '\\', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', ' ', ' ']
allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_-'
settings = {'xms': 512, 'xmx': 1024, 'session': 12345, 'path_jre_bin': 'path/to/jre/bin', 'nickname': 'Player'}

def start():
    global nickname
    nickname_text = nickname.get()
    if any(char not in allowed_chars for char in nickname_text):
        showerror("Error", "Nickname contains invalid characters.")
        return
    # Rest of the start function...

def main():
    global nickname
    root = Tk()
    root.title(f"{name} {ver}")
    root.geometry("320x240")
    root.resizable(False, False)

    txtlogo = Label(root, text=name)
    nickname = Entry(root)

    start_button = Button(root, text="Играть!", command=start, cursor="hand2")

    txtlogo.pack()
    nickname.pack()
    start_button.pack()

    root.mainloop()

main()

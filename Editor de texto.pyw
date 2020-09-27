from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Editor de texto')

ruta = ''

def Licencia():
    messagebox.showwarning("Estado licencia", "Producto bajo licencia GNU")
def twitter():
    messagebox.showinfo("Twitter", "https://twitter.com/ElSabalero101")
def Info():
    messagebox.showinfo("Procesador de Fran", "Procesador de texto version 1.0 / 2019")
def Salir():
    valor = messagebox.askquestion("Salir", "¿Desea salir?") #askokcancel para aceptar o cancelar (bool)
    if valor == 'yes':
        root.destroy()
def OpenFile():
    global ruta

    ruta = filedialog.askopenfilename(initialdir = 'C:\\Users\\Usuario\\Desktop', filetypes = (("Ficheros de texto", "*.txt"),
    ("Todos los ficheros", "*.*")))

    if ruta != '':
        theFile = open(ruta, 'r')
        contenido = theFile.read()
        text.delete(1.0, END)
        text.insert('insert', contenido)
        theFile.close()
        root.title(ruta + '- Editor de texto')
def SaveFile():
    global ruta

    if ruta != '':
        contenido = text.get(1.0, 'end-1c')
        theFile = open(ruta, 'w+')
        theFile.write(contenido)
        theFile.close()
        messagebox.showinfo("Guardado", "Fichero guardado correctamente")
    else:
        SaveAsFile()
def SaveAsFile():
    global ruta

    theFile = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    ruta = theFile.name

    if theFile is not None:
        contenido = text.get(1.0, 'end-1c')
        theFile = open(ruta, 'w+')
        theFile.write(contenido)
        theFile.close()
        messagebox.showinfo("Guardado", "Fichero guardado correctamente")
    else:
        messagebox.showerror("Guardado", "Guardado cancelado")
def NewFile():
    global ruta

    text.delete(1.0, END)
    root.title('Editor de texto')
    ruta = ''


MenuBar = Menu(root)
root.config(menu = MenuBar, width = 300, height = 200)

arch_menu = Menu(MenuBar, tearoff = 0)
arch_menu.add_command(label = 'Nuevo', command = NewFile)
arch_menu.add_command(label = 'Cargar', command = OpenFile)
arch_menu.add_command(label = 'Guardar', command = SaveFile)
arch_menu.add_command(label = 'Guardar como', command = SaveAsFile)
arch_menu.add_separator()
arch_menu.add_command(label = 'Salir', command = Salir)

ed_menu = Menu(MenuBar, tearoff = 0)
ed_menu.add_command(label = 'Copiar')
ed_menu.add_command(label = 'Cortar')
ed_menu.add_command(label = 'Pegar')

tools_menu = Menu(MenuBar, tearoff = 0)

h_menu = Menu(MenuBar, tearoff = 0)
h_menu.add_command(label = 'Licencia', command = Licencia)
h_menu.add_command(label = 'Twitter', command = twitter)
h_menu.add_command(label = 'Acerca de ...', command = Info)

MenuBar.add_cascade(label = 'Archivo', menu = arch_menu)
MenuBar.add_cascade(label = 'Edición', menu = ed_menu)
MenuBar.add_cascade(label = 'Herramientas', menu = tools_menu)
MenuBar.add_cascade(label = 'Ayuda', menu = h_menu)

frame = Frame(root)
frame.pack()

text = Text(frame, width = 50, height = 25)
text.grid(row = 0, column = 0)
scroll = Scrollbar(frame, command = text.yview)
scroll.grid(row = 0, column = 1, sticky = 'nsew')
text.config(yscrollcommand = scroll.set, font = ("Consolas", 12))

root.mainloop()
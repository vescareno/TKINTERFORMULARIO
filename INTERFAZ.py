from tkinter import *
from tkinter import ttk
import tkinter as tk

raiz = Tk()
raiz.title("Muestra Widgets")
raiz.geometry("500x400")

marcoPrincipal = ttk.Frame(raiz)
marcoPrincipal.grid(column=0, row=0)


marco2= ttk.Frame(marcoPrincipal, width=400, height=400)
marco2.grid(column=0, row=0, columnspan=4, rowspan=5)


tk.Radiobutton(marcoPrincipal, text="Estudiante").grid(column=5, row=0)
tk.Radiobutton(marcoPrincipal, text="Empleado").grid(column=5, row=1)
tk.Radiobutton(marcoPrincipal, text="Desempleado").grid(column=5, row=2)
tk.Button(marcoPrincipal, text="Guardar").grid(column=1, row=7)
tk.Button(marcoPrincipal, text="Cancelar").grid(column=2, row=7)
comboEstados = ttk.Combobox(marcoPrincipal, textvariable=StringVar())
comboEstados.grid(column=4, row=5, columnspan=2, rowspan=2, padx=15)
comboEstados['values']= ("Aguascalientes", "Baja California", "Baja california sur", "Campeche", "Coahuila")


ttk.Label(marco2, text="A. Paterno").grid(column=0, row=1, sticky=W)
txtAPaterno= ttk.Entry(marco2, textvariable=StringVar(), width=25)
txtAPaterno.grid(column=1, row=1, columnspan=3, sticky=E)

ttk.Label(marco2, text="A. Materno").grid(column=0, row=2, sticky=W)
txtAMaterno= ttk.Entry(marco2, textvariable=StringVar(), width=25)
txtAMaterno.grid(column=1, row=2, columnspan=3, sticky=E)


ttk.Label(marco2, text="Correo").grid(column=0, row=3, sticky=W)
txtAMaterno= ttk.Entry(marco2, textvariable=StringVar(), width=25)
txtAMaterno.grid(column=1, row=3, columnspan=3, sticky=E)

ttk.Label(marco2, text="Móvil").grid(column=0, row=4, sticky=W)
txtAMaterno= ttk.Entry(marco2, textvariable=StringVar(), width=25)
txtAMaterno.grid(column=1, row=4, columnspan=3, sticky=E)

marco3= ttk.Frame(marcoPrincipal, relief="raised")
marco3.grid(column=0, row=5, columnspan=4, rowspan=2, padx=10, pady=10, sticky=EW)
ttk.Label(marco3, text="Aficiones: ").grid(column=0, row=5, columnspan=4, sticky=W)
Leer = ttk.Checkbutton(marco3, text="Leer").grid(column=0, row=6)
Música = ttk.Checkbutton(marco3, text="Música").grid(column=1, row=6)
Videojuegos = ttk.Checkbutton(marco3, text="Videojuegos").grid(column=2, row=6, columnspan=2)



raiz.mainloop()
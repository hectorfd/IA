import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1280x720')
ventana.title('Ventana de Hector')
ventana.config(background='#f97e72')

# Manejo de grid(regjilla o cuadricula)
boton1 = ttk.Button(ventana, text = 'boton1')
boton2 = ttk.Button(ventana, text = 'boton2')
boton3 = ttk.Button(ventana, text = 'boton3')
boton4 = ttk.Button(ventana, text = 'boton4')
boton5 = ttk.Button(ventana, text = 'boton5')
boton6 = ttk.Button(ventana, text = 'boton6')

# grids para organizar los botones
boton1.grid(row = 0, column = 0)
boton2.grid(row = 0, column = 1)
boton3.grid(row = 0, column = 2)


boton4.grid(row = 1, column = 0)
boton5.grid(row = 2, column = 0)
boton6.grid(row = 3, column = 0)

# configurar grids
#columnconfigure es para configurar el peso de las columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=10)
ventana.columnconfigure(2, weight=1)

# para el peso de las filas usaremos row

ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=10)
ventana.rowconfigure(3, weight=1)


ventana.mainloop()
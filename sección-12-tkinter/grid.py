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

# grids para organizar los botones
boton1.grid(row = 0, column = 0)
boton2.grid(row = 1, column = 0)
boton3.grid(row = 0, column = 1)

ventana.mainloop()
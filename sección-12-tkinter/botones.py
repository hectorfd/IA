import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1280x720')
ventana.title('Ventana de Hector')
ventana.config(background='#f97e72')

def saludar(name):
    print(f'Te saludan jojojo {name}')

# botones con tkinter
# para mandar parametros debemos usar lambda
boton = ttk.Button(ventana, text = 'Presioname', command=lambda: saludar('Hector'))# no se llama () porque queremos que se ejecute infinitamente
boton.pack(pady=20)


ventana.mainloop()
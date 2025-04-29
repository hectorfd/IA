import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1280x720')
ventana.title('Ventana de Hector')
ventana.config(background='#f97e72')

# funcion para enviar texto
def enviar():
    label['text'] = caja_texto.get()

# cajas de texto
caja_texto = ttk.Entry(ventana)
caja_texto.pack(pady=20)
# colocamos el boton

boton = ttk.Button(ventana, text='Enviar', command=enviar)
boton.pack(pady=20)

# label donde habra el texto ingresado

label = ttk.Label(ventana, text = '')
label.pack(pady=20)



ventana.mainloop()
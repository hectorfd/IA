import tkinter as tk
# una de las mejoras de los comonentes es ttk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1280x720')
ventana.title('Ventana de Hector')
ventana.config(background='#f97e72')
# creamos una eqiqueta llamada tambien label
label = ttk.Label(ventana, text = 'primer texto')# modificamos el tk por el ttk para que tenga mas funcionalidades
label.pack()# esto empaqueta la etiqueta y la muestra en la ventana
#para acomodar la etqueta
label.pack(pady=20)
# paramodificar el texto de la eqitqueta
label['text'] = 'cambiando el primer texto:' #? text es una propiedad de la etiuqeta que permite cambiar el texto





ventana.mainloop()

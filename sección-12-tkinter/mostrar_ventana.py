import tkinter as tk

# crear ventana
ventana = tk.Tk()
# redimensionamos
ventana.geometry('1280x720')
# poner titulo
ventana.title('Ventana de Hector')
# evitar que se redimensione
ventana.resizable(0, 0)
# modificar el color de la ventana
ventana.config(background='#f97e72')
# hacer visible ventana
ventana.mainloop()

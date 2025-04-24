from monitor import Monitor
from dispositivos_entrada import Ratones
from dispositivos_entrada import Teclados

class Computadora:
    count_computadora = 0
    def __init__(self, name):
        self.name = name
        self.list_mouse = []
        self.list_keyboard = []
        self.list_monitor = []
        Computadora.count_computadora += 1
        self.id_computadora = Computadora.count_computadora
        
    @classmethod
    def get_total_computadoras(cls):
        return cls.count_computadora
    
    # agregacion monitor
    def add_monitor(self, brand, size):
        monitor = Monitor(brand, size)
        self.list_monitor.append(monitor)
        
        
    # agregacion raton
    def add_raton(self, brand, type_input):
        raton = Ratones(brand, type_input)
        self.list_mouse.append(raton)
        
    # agregacion teclado
    def add_teclado(self, brand, type_input):
        teclado = Teclados(brand, type_input)
        self.list_keyboard.append(teclado)
        
    
    def __str__(self):
        return f"Id: {self.id_computadora}, Name: {self.name}"
        
class DispositivoEntrada:
    def __init__(self, brand, type_input):
        self.brand = brand
        self.type_input = type_input
        
class Raton(DispositivoEntrada):
    count_mouse = 0
    def __init__(self, brand, type_input):# es necesario poner lo mismo que la clase padre porque heredamos atributos
        Raton.count_mouse +=1
        self.id_mouse = Raton.count_mouse
        super().__init__(brand, type_input)# super llama al constructor de la clase padre
    @classmethod
    def get_total_mouses(cls):
        return cls.count_mouse
    def __str__(self):
        return f"Id: {self.id_mouse}, Brand: {self.brand}, Type Input: {self.type_input}"
        
class Teclado(DispositivoEntrada):
    count_keyboard = 0
    def __init__(self, brand, type_input):
        Teclado.count_keyboard +=1
        self.id_keyboard = Teclado.count_keyboard
        super().__init__(brand, type_input)
    @classmethod
    def get_total_keyboards(cls):
        return cls.count_keyboard
    def __str__(self):
        return f"Id: {self.id_keyboard}, Brand: {self.brand}, Type Input: {self.type_input}"
        
        
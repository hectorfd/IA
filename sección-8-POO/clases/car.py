# Probando encapsulamiento
class Car:
    def __init__(self, brand, model, color):
        self.__brand = brand #! public atribute
        self.__model = model #! protected atribute
        self.__color = color #! private atribute estos solo son modificados por get y set
    
    def drive(self):
        print(f'carro: {self.__brand}\nModelo: {self.__model}\nColor: {self.__color}')
    
    def get_brand(self):
        return self.__brand # retorna el valor de la marca del carro
    
    def set_brand(self, brand):# toma como parametro el valor de la marca del carro para ser modificado
        self.__brand = brand # modifica el valor de la marca del carro
    
    def get_model(self):
        return self.__model
    
    def set_model(self, model):
        self.__model = model
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
        
# main program
def main():
    car1 = Car('Chevrolet', '2025', 'guinda')
    car1.drive()
    
    car1.set_brand('Toyota')
    car1.set_model('2026')
    car1.set_color('rojo')
    
    car1.drive()
    
    car2 = Car('Ford Mustang', '1969', 'gris oscuro')
    print(car2.get_brand())
main()
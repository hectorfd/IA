# esta sera la clase Padre
class Animal:
    def comer(self):
        print('El animal come')
    def dormir(self):
        print('El animal duerme')


    
# esta sera la clase Hija

class Perro(Animal):
    def sonido(self):
        print('El perro ladra')
    # sobreescribiendo dormir
    def dormir(self):
        print('el perro duerme 12 horas')
        
# probaremos polimorfismo

class Gato(Animal):
    def sonido(self):
        print('El gato maulla')
        
        
# creamos el objeto
mishon = Gato()
berlin = Perro()
berlin.comer()
berlin.dormir()
# ambos metodos de polimorfismo tienen el mismo nombre pero hacen cosas diferentes
berlin.sonido()# polimorfismo el perro ladra
mishon.sonido() # polimorfismo el gato maulla



# clase objet 
class Persona: 
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    #sobreescribir el metodo __str__ __= dunder
    def __str__(self):
        return f'Name: {self.name} - Last Name: {self.last_name}'
    
# probando objet

persona1 = Persona('Juan', 'Rodriguez')
print(persona1.__str__())# nos muestra el nombre y apellido de la funcion str
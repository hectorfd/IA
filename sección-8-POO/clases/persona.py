#definicion
# se recomienda Camel Case para las clases
class Persona:
    # constructor
    def __init__(self, name, last_name):
        #atributos
        self.name = name
        self.last_name = last_name
    
    # esta opcion ya no se usa por el hecho de que crea objetos vacios en un inicio
    # def init_persona(self, name, last_name):
    #     #atributos
    #     self.name = name
    #     self.last_name = last_name
        
    def show_contacto(self):
        print(f'Name: {self.name}\nLast name: {self.last_name}')

    
# objetos de clase
def main():
    # persona1 = Persona()# es un objeto vacio
    # persona2 = Persona()
    # son los rastros de lo que fue init_persona ya no se usa
    # persona1.init_persona('Hector', 'Ferro Dávalos')
    # persona2.init_persona('Jesús', 'de Nazaret')
    persona1 = Persona('Hector', 'Ferro Dávalos')# este objeto ya no inicializa vacio
    persona2 = Persona('Jesús', 'de Nazaret')
    persona1.show_contacto() 
    persona2.show_contacto()

main()
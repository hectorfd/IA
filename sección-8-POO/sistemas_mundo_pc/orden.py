from computadora import Computadora
class Orden:
    count_orden = 0
    def __init__(self):
        self.list_computadoras = []
        Orden.count_orden += 1
        self.id_orden = Orden.count_orden
    
    
    # agregar computadoras
    def add_computadora(self, name):
        computadora = Computadora(name)
        self.list_computadoras.append(computadora)
        
    # mostrar computadoras
    def show_computadoras(self):
        for computadora in self.list_computadoras:
            print(computadora)
    
    def __str__(self):
        computadoras_str = "\n".join(str(computadora) for computadora in self.list_computadoras)
        return f"Id: {self.id_orden},\n List: {computadoras_str}"
        
        
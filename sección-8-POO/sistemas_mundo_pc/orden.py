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
        
    # mostrar computadora con detalles de teclado, raton y monitor
    def show_computadoras(self):
        for computadora in self.list_computadoras:
            print(computadora)
    
    def __str__(self):
        orden_info = f"Orden #{self.id_orden}:\n"
        for computadora in self.list_computadoras:
            orden_info += f"- {computadora}\n"  # Llama a __str__ de Computadora
        orden_info += f"Total de computadoras: {len(self.list_computadoras)}"
        return orden_info
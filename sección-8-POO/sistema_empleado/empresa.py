from empleado import Empleado # importamos la clase Empleado
# porque la utilizaremos para crear objetos de tipo empleado 
# a esto se le conoce en POO como instanciación
class Empresa:
    def __init__(self, name):
        self.name = name
        # employees es un atributo de instancia de la clase Empresa
        self.list_employees = [] 
    # esta es una relacion de agregacion y composicion entre Empresa y Empleado
    def add_employees(self, name, department):# esta funcion agregara un empleado a la lista de empleados
        worker = Empleado(name, department)# se crea un objeto gracias a la instanciacion de la clase Empleado
        self.list_employees.append(worker)# con esto se agrega el objeto al atributo list_employees
        
    def get_number_employees(self, department):# esta funcion devolvera el numero de empleados por departamento
        count_by_department = 0 
        for employee in self.list_employees:
            if employee.department == department:
                count_by_department += 1
        return count_by_department
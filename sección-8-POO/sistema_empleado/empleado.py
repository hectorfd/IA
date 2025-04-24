class Empleado:
    count_employees = 0 # es un atributo de clase
    def __init__(self, name_employee, department):
        self.name_employee = name_employee
        self.department = department
        Empleado.count_employees += 1 # se usa antes Empleado para referirse a la clase
        
    # usaremos una etiqueta de classmethod para acceder a la variable de clase count_employees
    @classmethod
    def get_total_employees(cls):
        return cls.count_employees # esta funcion permitira acceder al atributo count_employees
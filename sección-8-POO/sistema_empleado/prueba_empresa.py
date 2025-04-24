from empresa import Empresa
print("Sistema Empresa y Empleados:")
# creamos el objeto a partir de la clase Empresa
company = Empresa('Multiservicios Sapitos S.A')

# agregamos empleados a la empresa
company.add_employees('Hector', 'Administración')
company.add_employees('Juan', 'Soporte')
company.add_employees('Pedro', 'Contabilidad')
company.add_employees('Maria', 'Contabilidad')

# imprimimos el numero de empleados por departamento

print(f'\tEL numero de empleados del departamento Contabilidad: {company.get_number_employees("Contabilidad")}')

empleados = ['Hector', 'Juan', 'Tomás']

ordenados = sorted(empleados)
print(ordenados)

# ordenamiento con lambda y sort

empleados_dict = [
    {'name': 'Hector', 'age': 25},
    {'name': 'Juan', 'age': 30},
    {'name': 'Tomás', 'age': 35}
]

empleados_ordenados = sorted(empleados_dict, key=lambda x: x['age'])
print(empleados_ordenados)
# Generadores sirven para optimizar el uso de memoria
# hay dos formas de crearlas 
# 1. Usando el generador
def generador_numeros(maximo):
    for i in range(maximo):
        yield i # yield en español es generador o produce

print(list(generador_numeros(5)))

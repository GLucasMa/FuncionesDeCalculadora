import math

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b==0:
        print("No es posible dividir por 0")
    else:
        return a / b
def potencia(a,b):
    return a ** b
def radicacionCuadrada(a):
    if a<0: 
        print("La raíz cuadrada de un número negativo, nos devuelve un valor fuera del conjunto de los reales")
    else:
        return math.sqrt(a)
def radicacionCubica(a):
    return a**(1/3)
def modulo(a, b):
    return a * (b/100)
def logaritmo(a, b=2.71828):

    # b es la base, si no se indica nada, se toma como logaritmo neperiano o base e
    # Pero a su vez la funcion nos pide dos valores, asi que le damos predeterminado
    # un aproximado del valor del numero "e"

    return math.log(a, b) 

def coseno(a):
    return math.cos(a)
def seno(a):
    return math.sin(a)
def tangente(a):
    return math.tan(a)
def radianes(a):
    return math.radians(a)



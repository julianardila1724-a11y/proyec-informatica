#esto es un comentario de una sola linea
"""Y ESTO ES UN COMENTARIO
 DE VARIAS LINEAS"""

#Inicializando variables
nombre="nombre del estudiante" 
edad=12
estado=True
nota=5.0

#Mostrar el contenido de las variables print()
print(nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#vamos a utilizar la funcion input para recojer datos por medio del teclado
nombre=input("¿como te llamas? ")
edad=input("¿que edad tienes? ")
estado=input("¿en que estado te encuentras? ")
nota=input("¿cual es tu nota? ")

#para visualizar que guardamos en las variables anteriores 
print("hola,",nombre,"un gusto conocerte")
print("tu edad es:",edad)
print("tu estado es:",estado)
print("tu nota es:",nota)
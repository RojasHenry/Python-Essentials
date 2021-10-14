# -*- coding: utf-8 -*-
"""
Curso Python Essentials 

Ejercicio 1
Parte - 1

Nombre: Henry Rojas

"""
# Encabezado
print("Empezando a trabajar con Python")
print("Realizado por: Henry Rojas")
print("Consultando los tipos de valores: \n")

# Prints de tipos de valores 
print("El tipo de dato de 875 es: \n",type(875))
print("El tipo de dato de 4.89 es: \n", type(4.89))
print("El tipo de dato del texto: Now is better than never. es: \n", type("Now is better than never."))
print("El tipo de dato de 1.32 es: \n", type(1.32))

# Prints de validación de tipo de valores
print("¿El valor 5 + 8j corresponde a un valor entero? \n", isinstance(5 + 8j, int))
print("¿El valor 8.2 corresponde a un valor entero? \n", isinstance(8.2, int))
print("¿El texto: Readability counts. corresponde a un string? \n", isinstance("Readability counts.", str))
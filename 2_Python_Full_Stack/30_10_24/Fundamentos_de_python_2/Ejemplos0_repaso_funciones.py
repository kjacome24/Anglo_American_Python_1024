# Condicionales ##########################################################################
# Los condicionales permiten ejecutar código dependiendo de si se cumplen ciertas condiciones.

numero1 = 50

if numero1 > 50:
    print("El número es mayor a 50")
elif numero1 == 50:
    pass  # No hace nada, solo pasa
else:
    print("El número es menor a 50")

# Otro ejemplo
edad = 18
if edad >= 18:
    print("Eres mayor de edad")  # Salida: Eres mayor de edad
else:
    print("Eres menor de edad")









# Funciones Comunes #######################################################################
# Estas son algunas funciones comunes que podemos usar para listas, diccionarios y números.

# Longitud de una lista
lista = [1, 2, 3, 4, 5]
print("Longitud de la lista:", len(lista))  # Salida: 5

# Valor mínimo y máximo en una lista
print("Valor mínimo:", min(lista))  # Salida: 1
print("Valor máximo:", max(lista))  # Salida: 5

# Suma de todos los elementos en una lista
print("Suma de la lista:", sum(lista))  # Salida: 15

# Tipo de dato de una variable
print("Tipo de lista:", type(lista))  # Salida: <class 'list'>

# Funciones para diccionarios
dic = {'name': 'Juan', 'age': 30, 'is_alive': True}
print("Llaves del diccionario:", dic.keys())  # Salida: dict_keys(['name', 'age', 'is_alive'])
print("Valores del diccionario:", dic.values())  # Salida: dict_values(['Juan', 30, True])
print("Items del diccionario:", dic.items())  # Salida: dict_items([('name', 'Juan'), ('age', 30), ('is_alive', True)])

# Sorting
lista = [1, 2, 5, 4, 3]
lista.sort()
print(lista)
lista_desc = sorted(lista, reverse=True)
print(lista_desc)



# Organizar por Llaves
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_by_keys = dict(sorted(my_dict.items()))
print("Sorted by keys:", sorted_by_keys)


# Ciclos (for, range y while) ##############################################################
# Los ciclos permiten repetir una serie de acciones varias veces.

# Ciclo for con range
for i in range(2, 10):
    print(i)  # Imprime del 2 al 9

# Ciclo for en una lista
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)  # Imprime cada elemento de la lista

# Ciclo for en un diccionario
dic = {'name': 'Juan', 'age': 30}
for key, value in dic.items():
    print(key, value)  # Imprime cada llave y valor del diccionario

# Ciclo while
contador = 0
while contador < 5:
    print("Contador:", contador)  # Salida: Contador desde 0 hasta 4
    contador += 1







# Funciones Básicas ########################################################################
# Las funciones permiten agrupar bloques de código reutilizables.

# Definición de una función de suma
def suma(a, b):
    return a + b

print("Suma de 2 y 3:", suma(2, 3))  # Salida: 5

# Función FizzBuzz
def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero

# Ejecutando la función FizzBuzz en un rango
for i in range(1, 16):
    print(fizz_buzz(i))  # Imprime Fizz, Buzz, FizzBuzz o el número según corresponda






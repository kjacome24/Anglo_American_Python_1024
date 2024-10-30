# Valores Booleanos ###################################################################
# Los valores booleanos solo pueden ser True o False, y son útiles para lógica condicional.
mayor = True
menor = False
print("Mayor:", mayor)  # Salida: True









# Números #############################################################################
# Puedes realizar operaciones aritméticas con números. Para usar un string como número, conviértelo con int().
numero1 = 10
numero2 = 20
numero3 = '30'
print("Suma de números:", numero1 + numero2 + int(numero3))  # Salida: 60









# Cadenas de Texto (Strings) ##########################################################
# Las cadenas se pueden concatenar o formatear usando .format(), f-strings o concatenación directa.
nombre = 'Juan'
apellido = 'Perez'

# Usando el método .format() para formatear cadenas
print("Hola soy {} {}".format(nombre, apellido))  # Salida: Hola soy Juan Perez

# Concatenación con +
print("Hola soy " + nombre + " " + apellido)  # Salida: Hola soy Juan Perez

# Usando f-strings para formateo rápido (Python 3.6+)
print(f'{nombre} {apellido}')  # Salida: Juan Perez







# Listas, Diccionarios y Tuplas #########################################################

# Listas
# Las listas son mutables (pueden cambiar) y pueden contener múltiples tipos de datos.
lista = [1, 2, 3, 4, 5]
lista_2 = ['a', 'b', 'c', 'd', 'e']

# Accediendo a elementos de la lista por índice
print("Primer elemento de lista:", lista[0])  # Salida: 1
print("Último elemento de lista_2:", lista_2[-1])  # Salida: e

# Modificando listas
lista.append(6)  # Agrega 6 al final de lista
print("Lista después de agregar 6:", lista)  # Salida: [1, 2, 3, 4, 5, 6]

# Usando pop para remover y retornar el último elemento
numero_extraido = lista.pop()  # Elimina 6
print("Último elemento eliminado de lista:", numero_extraido)  # Salida: 6
print("Lista después de pop:", lista)  # Salida: [1, 2, 3, 4, 5]

# Usando pop con índice para eliminar un elemento específico
numero_extraido_elegido = lista.pop(2)  # Elimina el elemento en el índice 2
print("Elemento eliminado en el índice 2:", numero_extraido_elegido)  # Salida: 3
print("Lista después de eliminar en índice 2:", lista)  # Salida: [1, 2, 4, 5]


# Eliminando elementos específicos con remove()
lista.remove(2)  # Elimina la primera ocurrencia de 2
lista_2.remove('c')  # Elimina 'c' de lista_2
print("Lista después de remover 2:", lista)
print("Lista_2 después de remover 'c':", lista_2)

# Eliminando elementos específicos con del
del lista[0]  # Elimina el primer elemento de lista
print("Lista después de eliminar el primer elemento:", lista)

# Insertando un elemento en una posición específica
lista_2.insert(2, 'f')  # Inserta 'f' en el índice 2
print("Lista_2 después de la inserción en índice 2:", lista_2)

# Cambiando elementos de la lista directamente
lista[1] = 10  # Cambia el segundo elemento a 10
print("Lista después de cambiar el segundo elemento:", lista)







# Tuplas #############################################################################
# Las tuplas son inmutables (no pueden cambiar) y se utilizan para almacenar múltiples elementos en una sola variable.
tupla = (1, 2, 3, 4, 5)
print("Primer elemento de tupla:", tupla[0])  # Salida: 1

# Nota: Las tuplas no soportan asignación de elementos o pop
# Descomentar la siguiente línea causará un error
# tupla[0] = 10  # Esto generará un error








# Diccionarios ########################################################################
# Los diccionarios almacenan pares clave-valor, lo que permite buscar un valor rápidamente mediante su clave.

person = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 30
}

# Accediendo a valores por clave
print("Nombre completo:", person['nombre'] + ' ' + person['apellido'])  # Salida: Juan Perez

# Agregando un nuevo par clave-valor
person['numero telefono'] = 123456789
print("Diccionario person después de agregar teléfono:", person)

# Modificando un valor existente
person['edad'] = 31  # Cambia 'edad' a 31
print("Diccionario person después de cambiar edad:", person)

# Eliminando un par clave-valor usando pop()
edad = person.pop('edad')  # Elimina 'edad'
print("Diccionario person después de eliminar edad:", person, "Edad eliminada:", edad)

# Usando del para eliminar un par clave-valor
del person['nombre']  # Elimina 'nombre'
print("Diccionario person después de eliminar nombre:", person)


# Elimina y devuelve el último par clave-valor con popitem()
ultimo = person.popitem()  # Elimina y devuelve el último par clave-valor
print("Último par clave-valor eliminado:", ultimo)  # Salida: ('numero telefono', 123456789)

# Usando clear para eliminar todos los elementos del diccionario
person.clear() # Elimina todos los elementos
print("Diccionario person después de clear:", person)  # Salida: {}

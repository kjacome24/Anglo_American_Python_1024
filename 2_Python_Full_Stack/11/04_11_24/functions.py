#################### Funciones intermedias (Core) ####################

##################### 1. Actualizar valores en diccionarios y listas ##############

# Tarea 1: Cambia el valor de 3 en matriz por 6.
# Resultado esperado después del cambio: [[10, 15, 20], [6, 7, 14]]

# Solución 1: Modificando la lista original directamente
matriz = [ [10, 15, 20], [3, 7, 14] ]

def function_x():
    for i in range(len(matriz)):
        # print(f'Estoy en la posicion {i}')
        for x in range(len(matriz[i])):
            # print(matriz[i][x])
            if matriz[i][x] == 3:
                matriz[i][x] = 6


function_x()

print(matriz)



# Solución 2: Usando bucles anidados para crear una nueva lista con el cambio deseado
matriz = [ [10, 15, 20], [3, 7, 14] ]

def function_y():
    new_list = [] # Lista nueva donde se almacenarán los valores actualizados
    for i in matriz:
        sub_list = []  # Lista temporal para cada sublista en matriz
        for x in i:
            if x == 3:
                sub_list.append(6)
            else:
                sub_list.append(x)
        new_list.append(sub_list)
    return new_list
        


print(function_y())





# Tarea 2: Cambia el nombre del primer cantante de "Ricky Martin" a "Enrique Martin Morales"

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]


def cambiar_nombre():
    for cantante in cantantes:
        if cantante["nombre"] == "Ricky Martin":
            cantante["nombre"] = "Enrique Mortin Morales"
    return cantantes

print(cambiar_nombre())


# Tarea 3: En ciudades, cambia “Cancún” por “Monterrey”

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

def cambiar_ciudad():
    for pais, ciudades_lista in ciudades.items():
        for i in range(len(ciudades_lista)):
            if ciudades_lista[i] == "Cancún":
                ciudades_lista[i] = "Moterrey"


cambiar_ciudad()

print(ciudades)


# Tarea 4: En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

def cambiar_latitud():
    for coord in coordenadas:
        coord["latitud"] = 9.9355431


xx = cambiar_latitud()

coordendas2 = coordenadas

print(coordendas2)






##################### 2. Iterar a través de una lista de diccionarios #####################

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


##Solucion sin bonus: 
# def iterarDiccionario(cantantes):
#     for x in range(0, len(cantantes)):
#         for key, value in cantantes[x].items():
#             print(key,value)


# iterarDiccionario(cantantes)


##Solucion con bonus: 
def iterarDiccionario(cantantes):
    for x in range(0,len(cantantes)):
        text = ''
        for key, value in cantantes[x].items():
            text += (key + "-" + value + ",")
        print(text)

iterarDiccionario(cantantes)








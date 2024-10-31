####################1

def contador_a_10():
    for i in range(0,101):
        print(i)

contador_a_10()

####################2


def contador_pares(inicio,final):
    for i in range(inicio,final+1):
        if i % 2 == 0:
            print(i)

contador_pares(1,10)


####################3


def ice_baby(inicio,final):
    for i in range(inicio,final+1):
        if i % 10 == 0:
            print(f"{i} baby")
        elif i % 5 == 0:
            print("ice ice")
        else:
            print(i)


ice_baby(1,30)

####################4


def suma_pares(inicio,final):
    counter = 0
    for i in range(inicio,final+1):
        if i % 2 == 0:
            counter += i
    print(counter)

suma_pares(1,50000)


####################5

def cuenta_regresiva(inicio,final,step):
    for i in range(inicio,final+1,step):
        print(i)

cuenta_regresiva(2024,-1,-3)

####################6


def multiplos(numInicial,numFinal,multiplo):
    for i in range(numInicial,numFinal+1):
        if i % multiplo == 0:
            print(i)


multiplos(3,10,2)

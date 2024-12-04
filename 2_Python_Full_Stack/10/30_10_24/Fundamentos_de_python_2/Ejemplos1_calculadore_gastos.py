def total_gastos():
    gastos = 0
    while True:
        gasto = input("Ingresa un monto:")
        if gasto == 'q':
            break
        gastos += int(gasto)
        print(f'El total de gastos es: {gastos}')
    

total_gastos()

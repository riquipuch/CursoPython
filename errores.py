try:
    op = int(input('Ingrese un numero: '))
    if type(op) == int:
        print('Usted selecciono un numero')
except TypeError:
    print('Ponga un numero')

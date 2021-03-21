op = int(input('Ingrese un numero: '))
try:
    if type(op) == int:
        print('Usted selecciono un numero')
except type(op) == str:
    print('Ponga un numero')

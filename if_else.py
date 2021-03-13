# If else

# Operadores


3 == 3
2 != 3
2 < 3
3 > 2
3 >= 2
1 <= 2

# Sintaxis del If:
edad = int(input('Ingrese la edad: '))
licencia = input('Tiene licencia: ')
print(type(licencia))

if edad >= 18:
    print('Es mayor')
    if licencia.upper() == 'SI':
        print('Tiene licencia')
    else:
        print('No tiene licencia')
elif edad <= 15 or edad > 10:
    print('Llamen a los papas')
elif edad == 10:
    print('Que haces acá?')

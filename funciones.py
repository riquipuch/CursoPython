def nombre(name, age):
    print(f'Hola {name}, vos tenés {age} años. Estoy dentro de la funcion')


# nombre('Ricardo', 21)

# Arbitrary Arguments, *args


def mi_funcion(*args):
    print(type(args))
    print('El más grande es ', args[2])


mi_funcion('Ricardo', 'Chevez', 'Vanessa', 'Mario', 48)

# Keyword Arguments


def mis_hijos(hijo1, hijo2, hijo3):
    print('Hijo 1: ', hijo1)
    print('Hijo 2: ', hijo2)
    print('Hijo 3: ', hijo3)


# mis_hijos(hijo1='Sháron', hijo3='Jorge', hijo2='Pablo')

# Arbitrary Keyword Arguments, **kwargs
def amigos(**kwargs):
    print('Mi mejor amigo es: ', kwargs['best'])
    print('Mi otro amigo es : ', kwargs['amigos_2'])


#amigos(best='Santiago', amigo_1='René', amigos_2='Carlos')


def nacionalidad(pais='Salvadoreño'):
    print('Yo soy ', pais)


def unidades_longitud(valor, valor2=100, unidades='SI'):
    if unidades == 'SI':
        print('El valor es ' + str(valor) + ' metros')
    elif unidades == 'ingles':
        print('El valor es ' + str(valor*0.3048) + ' ft')
    print(valor2)


# unidades_longitud(50, unidades='ingles')


# Ejercicio Conversion de unidades:
def convertidor(valor, sistema=1, tipo='longitud'):
    if tipo == 'longitud':
        if sistema == 1:
            print(valor)
        elif sistema == 2:
            print(valor * 0.3048)
    elif tipo == 'velocidad':
        if sistema == 1:
            print(valor)
        elif sistema == 2:
            print('La velocidad es: [ft/s]')
            print(valor * 1000/(3600*0.3048))


#convertidor(50, sistema=2, tipo='velocidad')
def elevar_cubo(n):
    return n ** 3



# Lambda
f = lambda n: n ** 0.5
g = lambda a, b, c=2: a * b/c


print(f(elevar_cubo(5)))
print(g(5,c=10,b=4))


print(type('Hola $1212'))
print(type(55+1.1))
print(type(55.645456))
print(type(True))
# Esto es un comentario
'''Este también es un 
comentario '''
# Iniciando el codigo
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
# Este es por concatenación
print('Bienvenido ' + nombre + '. Vos tenés' + str(edad) + 'años')
# Este es por format
print(f'Bienvenido {nombre}. Vos tenés {edad} años')
nombre_completo = nombre + apellido
print(nombre_completo[:5])  # Desde el inicio a la posición 5
print(nombre_completo[1:5])  # Desde la 1 hasta la 5
print(nombre_completo[5:])  # Desde la 5 hasta el final
print(nombre_completo[-1])  # Acceder al último elemento
#
x = 1e5
print(2+2)
print(2*5)
print(2/4)
print(2-6)
print(2 ** 5)
# Esta es otra manera de elevar un número a una potencia
# Primero se escribe la base y luego el exponente (base, exponente)
print(pow(2, 3))

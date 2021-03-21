# While loops
i = 1
while i < 6:
    print(i)
    #i = i + 1
    i += 1

while i < 10:
    print(i)
    i += 2
else:
    print('Ya no estoy dentro del while')

while True:
    print('Estoy dentro del while')
    op = int(input('Ingrese una opcion para salir: 1. Salir 0. Quedarse'))
    if op == 1:
        break
    else:
        pass


# For loops
frutas = ['manzana', 'banana', 'naranja', 'peras', 'mango']
for fruta in frutas:
    print(fruta)

for i in range(len(frutas)):
    print(i)

for letra in 'manzana':
    print(letra)

for numero in range(1, 8):
    print(numero)

for numero in range(2, 40, 5):
    print(numero)


# Ejercicio
'''Introducir una contraseña hasta que sea válida'''

password = 'contraseña123'

while True:
    x = input('Ingrese la contraseña: ')
    if x == password:
        print('Contraseña correcta!')
        break
    else:
        print('Escriba bien la contraseña')

# Ejercicio 2:

frase = input('Ingrese la frase: ')
letra = input('Ingrese la letra: ')
cont = 0
for i in frase:
    if i == letra:
        cont += 1
print(f'Había {cont} veces la letra {letra}')

# Ejercicio 3: Escribir un numero y retornar los impares
n = int(input('Ingrese el número: '))
for i in range(1, n+1, 2):
    print(i, end=' ')

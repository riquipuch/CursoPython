# tipo de dato: Lista
lista_1 = []
lista_2 = ['Hola', 'Ricardo', 25.44987, False, 'Ricardo']
print(lista_2)
# Longitud de la lista
print(len(lista_2))
lista_3 = [[1, 2, 3], [7, 8, 9], [4, 5, 6], 'Ricardo', 21, 'Azul']
print(lista_3)
# Accediendo datos de la lista
lista_3[1][1] = 89
print('Ricardo' in lista_3)
# Remover elemento de la lista
lista_3.remove(21)
print(lista_3)
# Eliminar el elemento dado el index
lista_3.pop(0)
print(lista_3)
# Agregar al final de la lista
lista_3.append('Rosado')
print(lista_3)
nombres = ['Ricardo', 'Frank', 'Eduardo', 'Sháron']
numero = [78, 56, 2, 4, 1208]
numero.sort(reverse=True)
nombres.sort(reverse=True)
print(nombres)
print(numero)
print('Cuantas veces: ', nombres.count('Ricardo'))
print('El index es: ', nombres.index('Eduardo'))
# Insertar un elemento dado el index y el elemento
lista_3.insert(2, 'Verde')
print(lista_3)

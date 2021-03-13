# Tipo de dato diccionario
dicc_1 = {'nombre': 'Quevedo'}
dicc_2 = {'nombre': ['Ricardo', 'Quevedo', 'Frank'], 'apellido': 'Quijada',
          'edad': 21, 'estudiante': True}
dicc_2['estatura'] = 1.73
print(dicc_2['nombre'][2])
dicc_2['diccionario'] = {'comida': 'pizza', 'deporte': 'futbol'}
print(dicc_2['diccionario'])
print(dicc_2['diccionario']['deporte'])
print(dicc_2.items())
print('Llaves del dict: ', dicc_2.keys())
print('Llaves del dict de dentro: ', dicc_2['diccionario'].keys())
print(dicc_2.values())
print(dicc_1.clear())
dic_nuevo = dicc_2.copy()
print(dic_nuevo)
print(dicc_2['diccionario'].get('deporte'))
dicc_2.pop('apellido')
print(dicc_2)

# Tipo de datos: Tuplas
tupla = ()
tupla_1 = ('Ricardo', 21, 1999, 1.73, True, ('Hola', 123))
tupla_2 = 'Ricardo', 2, True
tupla_3 = (5,)
tupla_4 = ('Quevedo', 'Frank', 'Sháron')
print(type(tupla_3))
# Funciones de la tupla
nueva_tupla = tupla_1 + tupla_2
print(nueva_tupla)
print(len(tupla_1))
print(nueva_tupla.count('Ricardo'))
print(nueva_tupla.index(21))
print(sorted(tupla_4))

# Tipo de dato: Sets
set_1 = {True, 23.45}
set_2 = {'Ricardo', 21, 'Python'}
print('Sháron' in set_2)
set_2.add(False)
print(set_2)
set_2.remove('Ricardo')
print(set_2)
set_3 = set_1.union(set_2)
print(set_3)
set_3.pop()
print(set_3)

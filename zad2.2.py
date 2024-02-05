import random
lista = []
for x in range(10):
    lista.append(random.randint(0,100))

print(lista)
lista_2 = []

for y in lista:
    if y % 2 == 0:
        lista_2.append(y)

print(lista_2)
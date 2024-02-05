def lista_abc(a: int, b: int, c: int):
    lista = list(range(a))
    tupla = tuple(range(b, c+1))
    lista_koncowa = []
    for x in lista:
        if x in tupla:
            lista_koncowa.append(x)

    print(lista_koncowa)


lista_abc(10, 1, 5)

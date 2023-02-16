"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        +01234
#        -54321
"""
string = "ABCDE"  # 5 caracteres (len)
lista = []
# lista = list()
print("1", bool([]))  # falsy
print("2", lista, type(lista))
"""

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
""" - Parte 01 - Aqui
lista = [123, True, "Luiz Otávio", 1.2, []]
lista[-3] = "Maria"
print("3", lista)
print("4", lista[2], type(lista[2]))
print(lista[4])
"""

"""" - Parte 02 - Aqui
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])
"""

""" - Parte 03 - Aqui
lista = [10, 20, 30, 40]
print(lista)
lista.append("Luiz")
print(lista)
nome = lista.pop()
print(lista)
lista.append(1233)
print(lista)
del lista[-1]
print(lista)
lista.clear()
print(lista)
lista.insert(100, 5)
print(lista)
print(lista[0])
"""

""" - Parte 04 - Aqui """
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(
    lista_b
)  # Não retorna nada e mexe diretamente na lista_a
print(lista_a)
print(lista_b)
print(lista_c)
print(lista_d)

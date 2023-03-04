"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = "Luiz"  # iterável

iteratador = texto.__iter__()  # iterator
# iteratador = iter(texto)  # iterator

while True:
    try:
        letra = iteratador.__next__()
        # letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)

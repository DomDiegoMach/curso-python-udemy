# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def operacoes(operacao):
    def multiplicar(numero):
        return print(operacao * numero)

    return multiplicar


d = operacoes(2)
t = operacoes(3)
q = operacoes(4)

d(2)
t(2)
q(2)

"""
def duplicar(numero):
    return 2 * numero


def triplicar(numero):
    return 3 * numero


def quadruplicar(numero):
    return 4 * numero


print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
"""

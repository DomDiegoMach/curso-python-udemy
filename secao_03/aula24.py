# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = "Otávio"
# print("print 1 - ", nome[2])
# print("print 2 - ", nome[-4])
# print("print 3 - ", "vio" in nome)
# print("print 4 - ", "zero" in nome)
# print("print 5 - ", 10 * "-")
# print("print 6 - ", "vio" not in nome)
# print("print 7 - ", "zero" not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")

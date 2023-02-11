"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) (maiúsculo e minúsculo)
"""
nome = "Luiz"
preco = 1000.95897643
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %08X" % (1500, 1500))
print("O hexadecimal de %d é %04X" % (15, 15))
print("O hexadecimal de %d é %0X" % (30, 30))

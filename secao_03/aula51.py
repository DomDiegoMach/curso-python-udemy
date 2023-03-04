"""
Introdução ao empacotamento e desempacotamento
"""
nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
print(nome2)

_, _, nome, *resto = ["Maria", "Helena", "Luiz"]
print(nome, resto)

nome, *resto = ["Maria", "Helena", "Luiz"]
print(nome, resto)

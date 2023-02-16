"""
Tipo tupla - Uma lista imutável
"""
nomes = ["Maria", "Helena", "Luiz"]
# nomes = tuple(nomes)
# nomes = list(nomes)
nomes = tuple(nomes)
print(type(nomes))
print(nomes[-1])
print(nomes.count("Maria"))
print(nomes.index("Luiz"))

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = "ABC"
print(f"1 - {variavel}")
print(f"2 - {variavel: >10}")
print(f"2 - {variavel:@>10}")
print(f"3 - {variavel: <10}.")
print(f"3 - {variavel:%<10}.")
print(f"4 - {variavel: ^10}.")
print(f"4 - {variavel:&^10}.")
print(f"5 - {1000.4873648123746:0=+10,.1f}")
print(f"6 - O hexadecimal de 1500 é {1500:08X}")
print(f"7 - {variavel!r}")

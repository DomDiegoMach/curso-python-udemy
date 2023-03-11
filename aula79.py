# Exemplo de uso dos sets
letras = set()
while True:
    letra = str(input("Digite: "))
    if len(letra) == 1:
        letras.add(letra.lower())
    elif letra in letras:
        print("Letra repetida")
    else:
        print("Digite apenas uma letra")

    if "l" in letras:
        print("PARABÉNS")
        break

    print(letras)

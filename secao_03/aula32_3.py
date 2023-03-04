"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input("Digite seu nome: ")


def tamanho_do_nome():
    try:
        nome_str = str(nome)
        if len(nome_str) <= 4:
            print("Seu nome é muito curto")
        elif len(nome_str) <= 6:
            print("Seu nome é normal")
        elif len(nome_str) > 6:
            print("Seu nome é muito grande")
    except ValueError:
        print(f"{nome} não é válido. Digite apenas letras")


tamanho_do_nome()

"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
"""

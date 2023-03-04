"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Que horas são ? ")


def pergunte_a_hora():
    try:
        hora_int = int(hora)
        if hora_int > 0 and hora_int <= 11:
            print("Bom dia")
        elif hora_int > 11 and hora_int <= 17:
            print("Boa Tarde")
        elif hora_int > 17 and hora_int <= 23:
            print("Boa Noite")
        else:
            print("Hora inválida")
    except ValueError:
        print(f"{hora} não é válido. Digite apenas números")


pergunte_a_hora()

"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""

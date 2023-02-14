for i in range(10):
    if i == 2:
        print("(1)", "i é 2, pulando...")
        continue

    # if i == 8:
    #     print("i é 8, seu else não executará")
    #     break

    for j in range(1, 3):
        print("(2)", i, j)
else:
    print("(3)", "For completo com sucesso!")

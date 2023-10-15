velocidade = int(input("Qual é a sua velocidade? "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 20
    print(f"Você foi multado! O valor da multa é {multa} R$.")
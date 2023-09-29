tamanho = int(input("Digite o tamanho da roupa: "))
cor = str(input("Digite uma cor para a roupa: "))

if tamanho >= 40 or cor == "preto":
    print("Quero comprar")
else:
    print("Não quero")
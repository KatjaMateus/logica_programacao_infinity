while True:
    usuario = str(input("Digite nome de usuário: "))
    senha = str(input("Digite senha: "))
    if usuario != senha:
        break
    else:
        print("Erro! Tente novamente.")
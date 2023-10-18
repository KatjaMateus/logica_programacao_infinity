
while True:
    nome = str(input("Digite nome: "))
    if len(nome) > 3:
        print(nome)
        break
    else:
        print("erro")

while True:
    idade = int(input("Digite a idade: "))
    if idade >= 0 or idade <= 150:
        print(idade)
        break
    else:
        print("erro")

while True:
    salario = float(input("Digite salário: "))
    if salario > 0:
        print(salario)
        break
    else:
        print ("erro")

while True: 
    sexo = str(input("Digite sexo: "))
    if sexo in ("FfMm"):
        print(sexo)
        break
    else:
        print("erro")

while True:
    civil = str(input("Digite estado civil: "))
    if civil in ("sScCvVdD"):
        print(civil)
        break
    else:
        print("erro")
    


genero = str(input("Qual é seu genero: [M ou F]? "))
if genero in "fF":
    print("F - Feminino")
elif genero in "mM":
    print("M - Masculino")
else:
    print("Genero inválido")
turno = str(input("Em qual turno você estuda? "))

if turno in "mM":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite")
else:
    print("Valor inválido")
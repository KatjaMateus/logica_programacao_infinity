turno = input("[M] - Manhã\n[V] - Tarde\n[N] - Noite\nEm qual turno você estuda? ")

if turno == "M" or turno == "m" or turno == "manha":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite")
else:
    print("Valor inválido")

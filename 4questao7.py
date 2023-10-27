maior_numero = cont = 0

while cont < 5:
    cont += 1
    num = int(input(f"Informe o {cont}º número: "))
    if maior_numero < num:
        maior_numero = num
print(f"O maior número foi {maior_numero}")

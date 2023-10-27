'''ano = 0
popA = int(input("Digite número de habitantes do país A: "))  
popB = int(input("Digite número de habitantes do país B: "))
taxaA = float(input("Digite a taxa de crescimento da pop A: "))
taxaB = float(input("Digite a taxa de crescimento da pop B: "))

tAcalc = (taxaA / 100) + 1
tBcalc = (taxaB / 100) + 1

if popA > popB or taxaA < taxaB:
    print("Digite números novamente. População A deve ser menor que B, e taxaA deve ser maior que taxaB")
    popA = int(input("Digite número de habitantes do país A: "))  
    popB = int(input("Digite número de habitantes do país B: "))
    taxaA = float(input("Digite a taxa de crescimento da pop A: "))
    taxaB = float(input("Digite a taxa de crescimento da pop B: "))
while popA < popB and taxaA > taxaB:
    popA *= tAcalc
    popB *= tBcalc
    ano += 1
print(f"Levarão {ano} anos para população A ultrapassar população B")'''

popA, popB  →  input (converter para inteiro)
taxaA, taxaB  →  input (converter para float)

população que começa menor precisa ter a maior taxa.

while True:
    popA = int(input('Informe a população inicial de A: '))
    popB = int(input('Informe a população inicial de B: '))

    taxaA = float(input('Informe a taxa de crescimento populacional anual de A: ')) + 1
    taxaB = float(input('Informe a taxa de crescimento populacional anual de B: ')) + 1

    condicao_certa = (popA > popB and taxaB > taxaA) or (popB > popA and taxaA > taxaB)
    maior_inicio = menor_inicio = tx_menor_inicio = tx_maior_inicio = 0
    if popA > popB:
        maior_inicio = popA
        tx_maior_inicio = taxaA
        menor_inicio = popB
        tx_menor_inicio = taxaB
    elif popB > popA:
        maior_inicio = popB
        tx_maior_inicio = tx_maior_inicio
        menor_inicio = popA
        tx_menor_inicio = taxaA
    else:
        print('As populações já começaram iguais.')
        break

    ano = 0
    if condicao_certa:
        while menor_inicio < maior_inicio:
            menor_inicio *= tx_menor_inicio
            maior_inicio *= tx_maior_inicio
            ano += 1
        print(f'Levarão {ano} anos, para ultrapassar.')
    else:
        print('Informe uma taxa maior para o país que começa com menos.')

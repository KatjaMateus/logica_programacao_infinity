ano = 0
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
print(f"Levarão {ano} anos para população A ultrapassar população B")

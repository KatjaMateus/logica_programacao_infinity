ano = 0
popA = int(input("Digite número de habitantes do país A: "))  
popB = int(input("Digite número de habitantes do país B: "))
taxaA = float(input("Digite a taxa de crescimento da pop A: "))
taxaB = float(input("Digite a taxa de crescimento da pop B: "))

tAcalc = (taxaA / 100) + 1
tBcalc = (taxaB / 100) + 1

    
while popA < popB and taxaA > taxaB:
    popA *= tAcalc
    popB *= tBcalc
    ano += 1
    print(f"Levarão {ano} anos para população A ultrapassar população B")
else: 
    print("Digite números novamente, população do país A deve ser menor do que população do país B, e taxa de crescimento do país A deve ser maior do que do país B")

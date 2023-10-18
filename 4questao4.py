Apop = 80000
Ataxa = 1.03
Acres = Apop * Ataxa
popA_ano = Acres * Ataxa


Bpop = 200000
Btaxa = 1.015
Bcres = Bpop * Btaxa
popB_ano = Bcres * Btaxa

while True:
    popA_ano += 1
    popB_ano += 1
    if popA_ano == popB_ano:
        break
    print(popA_ano)
    


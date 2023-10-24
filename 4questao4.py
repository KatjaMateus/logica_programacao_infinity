ano = 0
popA = 80000
taxaA = 1.03
popB = 200000
taxaB = 1.015
    
while popA < popB:
    popA *= taxaA
    popB *= taxaB
    ano += 1

    '''print(f"Ano {ano}")
    print(f"População A {popA}")
    print(f"Populaçã B {popB}")'''

print(f"Levarão {ano} para a população do país A ultrapassar da população do país B")
    


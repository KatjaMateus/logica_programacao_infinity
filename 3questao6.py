'''
Número primo -> divisível apenas por 1 e ele mesmo
Então números primos têm apenas 2 divisores
'''

numero = int(input('Digite um número para ser verificado: '))
divisores = 0

for i in range(1, numero + 1):
    print(i)
    if numero%i == 0:
        divisores += 1

if divisores == 2:
    print(f'{numero} é primo')
else:
    print(f'{numero} não é primo, pois possui {divisores} divisores.')

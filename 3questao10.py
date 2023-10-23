frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
#inverso = ""
#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
inverso = junto[::-1]
if inverso == junto:
    print("Temos um palíndromo")
else:
    print("Não é um palíndromo: ")

'''frase = input('Digite uma palavra: ').strip().upper()
palavras = frase.replace(' ', '')

--------------
OPÇÃO 1:
ultimo_indice = len(palavras)-1
for indice in range(ultimo_indice, -1, -1):
    # para acessar a posição: lista[indice]
    print(palavras[indice])

OPÇÃO 2:
inverso = palavras[::-1]
--------------

if palavras == inverso:
    print('É palíndromo')
else:
    print(f'Não é palíndromo. O inverso é {inverso}.')
'''

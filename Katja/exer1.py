#n = int(input("Digite um número: "))
#for c in range(0, n +1):
#    print(c)
#print("FIM")

'''i = int(input("Digite um númro: "))
f = int(input("Digite um número: "))
p = int(input("Digite o passo: "))
for c in range(i, f+1, p):
    print(c)'''

'''sum = 0
for c in range(0, 5):
    n = int(input("Digite a nota: "))
    sum += n
print(sum / 5)'''

'''for c in range(1, 51):
    if c % 2 == 0:
        print(c)'''

#48
'''soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(soma)
print(cont)'''

#49
'''num = int(input("Digite um número para ver a sua tabuada: "))
for c in range(1, 11):
    print(f"{num} x {c} = {num*c}")'''

#50
'''soma = 0
cont = 0
for c in range(0, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(soma)'''

#53
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




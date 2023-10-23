cont = 0
palavra = "kampaaja"
for letra in palavra:
    if letra not in "aeiou":
        cont += 1
print(cont)

'''cont = 0
palavra = input('Digite uma palavra: ')

for letra in palavra:
    if letra in 'aeiou':
        pass
    else:
        cont += 1
print(f'Há {cont} consoantes em {palavra}')'''

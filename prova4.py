cont1 = 0
cont2 = 0
soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    cont1 += 1
    cont2 += num
    media = cont2 / cont1
print(f"A quantidade de números é {cont1}, a soma deles é {cont2} e a media é {media}")



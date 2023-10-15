numero1 = int(input("numero1: "))
numero2 = int(input("numero2: "))
numero3 = int(input("numero3: "))

if numero1> numero2 and numero1> numero3 :
    if numero2>numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)

elif numero2 > numero1 and numero2 > numero3:
    if numero1>numero3:
        print(numero2, numero1, numero3)
    else:
        print(numero2, numero3, numero1)

else:
    if numero2>numero1:
        print(numero3, numero2, numero1)
    else:
        print(numero3, numero1, numero2)

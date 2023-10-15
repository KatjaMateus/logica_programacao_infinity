produto1 = float(input("preço do produto 1: "))
produto2 = float(input("preço do produto 2: "))
produto3 = float(input("preço do produto 3: "))

if produto1 < produto2 and produto1 < produto3:
    print("Compre o produto1")
elif produto2 < produto1 and produto2 < produto3:
    print("Compre o produto2")
else:
    print("Compre o produto3")

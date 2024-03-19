fruta = input("Fruta: ")
fruta = fruta.lower()
if(fruta == "banana"):
    print(f"O preço da {fruta} por quilo é : 5,23")
elif(fruta == "maça" or fruta == "maca"):
    print(f"O preço da {fruta} por quilo é : 12,10")
elif(fruta == "cereja"):
    print(f"O preço da {fruta} por quilo é : 58,00")
else:
    print(f"Não temos o preço da da {fruta}")
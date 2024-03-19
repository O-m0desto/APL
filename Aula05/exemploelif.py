fruta = input("Fruta: ")
fruta = fruta.lower()
if(fruta == "banana"):
    print("O preço dessa fruta por quilo é : 5,23")
elif(fruta == "maça" or fruta == "maca"):
    print("O preço dessa fruta por quilo é : 12,10")
elif(fruta == "cereja"):
    print("O preço dessa fruta por quilo é : 58,00")
else:
    print("Não temos essa fruta")
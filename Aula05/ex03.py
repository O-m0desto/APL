lado1 = float(input("Informe o comprimento do 1º lado: "))
lado2 = float(input("Informe o comprimento do 2º lado: "))
lado3 = float(input("Informe o comprimento do 3º lado: "))

if(((lado1 + lado2) < lado3)or((lado3 + lado2) < lado1))or((lado3 + lado1) < lado2):
    realidade= False
else:
    realidade = True

if realidade == True:
    if(lado1==lado2==lado3):
        print("O triangulo formado é Equilátero")
    elif(lado1!=lado2!=lado3):
        print("o triangulo formado é Escaleno")
    else:
        print("o triangulo formado é Isósceles")
else:
    print("Estes valores não formam um triangulo")
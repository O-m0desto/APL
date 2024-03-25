comprimento = float(input("Informe o valor do comprimento do aposento: "))
largura = float(input("Informe o valor da largura do aposento: "))
qtdLitros = int(input("Informe a quantidade de tinta em litros: "))

area_porta = 0.80 * 2.10
area_parede = (comprimento * largura)
area_para_pintar = ((area_parede*4) - area_porta)

if (area_para_pintar % 3 >= 1):
    qtdLatasNecessarias = (area_para_pintar//3 + 1)
else:
    qtdLatasNecessarias = area_para_pintar / 3

print(f"A quantidade de litros necessários para pintar o comodo são de {qtdLatasNecessarias/3} litros de tinta")

if(qtdLitros > qtdLatasNecessarias):
    print("E você já possui a mais que a quantidade necessária de tinta")
elif(qtdLitros == qtdLatasNecessarias):
    print("e você possui a quantidade exata necessaria de tinta")
else:
    print(f"então você tem de comprar {qtdLatasNecessarias - qtdLitros} litros de tinta")

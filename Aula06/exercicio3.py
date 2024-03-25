comprimento = float(input("Informe o valor do comprimento do aposento: "))
largura = float(input("Informe o valor da largura do aposento: "))
qtdLitros = int(input("Informe a quantidade de tinta em litros: "))

area_porta = 0.80 * 2.10
area_parede_1 = (comprimento * 2.80)
area_parede_2 = (largura * 2.80)
area_paredes = 2*(area_parede_1 + area_parede_2)
area_para_pintar = area_paredes - area_porta

if (area_para_pintar % 3 >= 1):
    qtdLatasNecessarias = (area_para_pintar//3 + 1)
else:
    qtdLatasNecessarias = area_para_pintar / 3

if (qtdLatasNecessarias % 3 != 1):
    qtdReal = (qtdLatasNecessarias//3) + 1
else:
    qtdReal = (qtdLatasNecessarias//3)


print(f"A quantidade de litros necessários para pintar o comodo são de {qtdReal} litros de tinta")

if(qtdLitros > qtdReal):
    print("E você já possui a mais que a quantidade necessária de tinta")
elif(qtdLitros == qtdReal):
    print("e você possui a quantidade exata necessaria de tinta")
else:
    print(f"então você tem de comprar {qtdReal - qtdLitros} litros de tinta")

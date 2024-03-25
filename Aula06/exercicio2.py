valortotal = float(input("Informe o valor da compra para fornecermos um desconto: "))

if(valortotal<1000):
    print(f"A sua compra com o desconto de {(valortotal/100)*10} ficara no total de: {valortotal - (valortotal/100)*10}")
elif(valortotal <5000):
    print(f"A sua compra com o desconto de {(valortotal/100)*20} ficara no total de: {valortotal - (valortotal/100)*20}")
else:
    print(
        f"A sua compra com o desconto de {(valortotal / 100) * 30} ficara no total de: {valortotal - (valortotal / 100) * 30}")
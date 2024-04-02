N = int(input("Informe um valor inteiro e positivo para calcular: "))

if (N%1 == 0) and (N>0):
    E = 0
    for i in range(1,N+1):
        E = E + 2**i
    print(f"O valor resultante é {E}")

    E = 0
    x = 1
    while (x <= N):
        E = E + 2**x
        x = x +1
    print(f"O valor resultante é {E}")
else:
    print("O valor informado não presta")
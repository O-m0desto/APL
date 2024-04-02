numero = int(input("Digite o número para calcular o fatorial: "))
resultado = 1
if numero > 0:
    for i in range(1,numero+1):
        resultado = i * resultado
    print(f"O fatorial de {numero} é {resultado}")
elif numero == 0:
    print("O fatorial de 0 é 1")
else:
    print("Não existe fatorial de números negativos")
#Usando FOR
alturatotal = 0
pesototal = 0
maiorimc=0
menorimc=999
qtdpessoas = int(input("Quantas pessoas vão participar? "))

for i in range (1,qtdpessoas+1):
    print("\n"*130)
    peso = float(input(f"Digite o peso da pessoa {i}: "))
    altura = int(input(f"Digite a altura da pessoa {i} em centimetros: "))
    alturatotal = alturatotal + altura
    pesototal = pesototal + peso
    altura = altura/100
    imc = peso/(altura**2)
    if menorimc > imc:
        menorimc = imc
    if maiorimc < imc:
        maiorimc = imc

print(f"O peso médio é de {pesototal/qtdpessoas}")
print(f"A altura média é de {alturatotal/qtdpessoas}")
print(f"O maior IMC é de {maiorimc}")
print(f"O menos IMC é de {menorimc}")


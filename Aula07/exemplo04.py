frase = input("Digite uma frase: ")
conta = 0
contaas = 0
vogais = 0
consoantes = 0
for caracter in frase:
    conta=conta+1
    if(caracter=="a" or caracter == "A" or caracter == "á" or caracter == "Á"):
        contaas = contaas + 1
    if caracter in 'AaáÁãÃEeÉeIiíÌÍOoóÓUuúÚ':
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1
print(f"A frase digitada contém {conta} digitos")
print(f"A frase digitada contém {contaas} A's digitados")
print(f"A frase digitada contém {vogais} vogais")
print(f"A frase digitada contém {consoantes} consoantes")
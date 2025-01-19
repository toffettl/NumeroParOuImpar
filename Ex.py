numero = input("Digite um número")

if  numero.isdigit(): #Verifica se é um número inteiro
    numero = int(numero)
    resto = numero % 2

    if resto == 0:
        print("Número par")
    else:
        print("Número ímpar")    
else:
    print("Seu número deve ser inteiro!")
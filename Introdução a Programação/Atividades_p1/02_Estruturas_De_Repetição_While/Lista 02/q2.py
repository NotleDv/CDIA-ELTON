valor = float(input("Digite um valor: "))

maior = valor
menor = valor
soma = valor

while (valor != -1):
    valor = float(input("Digite um valor: "))
    if valor == -1:
        break
    
    elif valor > maior:
        maior = valor
        
    elif valor < menor:
        menor = valor

    soma += valor
    
print(f"\nMaior valor: {maior}\nMenor valor: {menor}\nTotal: {soma}")
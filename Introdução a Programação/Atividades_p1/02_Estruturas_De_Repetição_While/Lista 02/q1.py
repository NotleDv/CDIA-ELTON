soma = 0

contador = 0
while (contador < 500):
    contador+=1
    if (contador%2) != 0:
        soma += contador

print(f"Soma dos impares até o 500: {soma}")
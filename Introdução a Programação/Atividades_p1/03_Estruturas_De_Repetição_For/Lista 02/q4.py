base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor da expoente: "))

temp = base
for i in range(1, expoente):
    base *= temp

print(f"Resultado: {base}")
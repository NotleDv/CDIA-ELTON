codigo = int(input("Digite um código: "))
total = 0
while (codigo != 0):
    if codigo == 1:
        quant = int(input("Digite a quantidade: "))
        total += quant*5.5
        
    elif codigo == 2:
        quant = int(input("Digite a quantidade: "))
        total += quant*2.3
        
    elif codigo == 3:
        quant = int(input("Digite a quantidade: "))
        total += quant*4.75
        
    elif codigo == 4:
        quant = int(input("Digite a quantidade: "))
        total += quant*6.8
        
    elif codigo == 5:
        quant = int(input("Digite a quantidade: "))
        total += quant*9.3
        
    else:
        print("Código inválido!")
    codigo = int(input("Digite um código: "))

print(f"Total: {total}")
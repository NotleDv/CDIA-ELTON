valor_1 = int(input("Valor um: "))
valor_2 = int(input("Valor dois: "))

contador = 0

while (valor_1 >= valor_2):
    valor_1 -= valor_2
    contador+=1

print(f"Quociente: {contador}") 
print(f"Resto: {valor_1}")
valor = float(input("Digite o valor: "))

b = 2
p = (b + (valor/b))/2

while (abs(b-p) > 0.0001):
    b = p
    p = (p + (valor/b))/2
    
print(f"Raiz de {valor} é aproximadamente: {p:.3}")    
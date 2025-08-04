aporte_int = float(input("Digite o valor de aporte: "))
taxa_juros = float(input("Taxa de juros: "))

ganho = 0
aporte_out = aporte_int
for i in range(24):
    aporte_out += aporte_int * (taxa_juros/100)  
    print(f"Valor mês {i+1}: {aporte_out}")   
    
print(f"Ganho: {aporte_out-aporte_int}")
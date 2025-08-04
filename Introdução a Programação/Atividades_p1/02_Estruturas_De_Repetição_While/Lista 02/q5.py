divida = float(input("Valor dívida: "))
juros_mensal = float(input("Juros mensal em %: "))
baixa_mensal = float(input("Valor a ser pago mensalmente: "))

count_meses = 0
total_juros = 0
total_pago = 0
juros = divida * (juros_mensal/100)

while (divida > baixa_mensal):
    divida = divida + juros - baixa_mensal
    total_juros += juros
    total_pago += baixa_mensal
    count_meses+=1

if divida > 0:
    total_pago += divida
    count_meses+=1
    
print(f"\nTotal pago: {(total_pago):.2f}")
print(f"Total juros pago: {total_juros:.2f}")
print(f"Total meses: {count_meses}")
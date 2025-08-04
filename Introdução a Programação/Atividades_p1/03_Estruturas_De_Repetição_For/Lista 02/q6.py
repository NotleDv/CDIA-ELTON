n = int(input("Digite um valor: "))

index_zero = 1

print("1", end="")

n_1 = 1
n_2 = 1
soma = 0
for i in range (n):
    print(end=", ")
    
    if i == 0:
        print(n_1, end="")
        
    else:
        print(f'{n_1+n_2}', end="")
        temp = n_1
        n_1 = n_2
        n_2 = n_2 + temp 
        # Tem que armazenar o n_1 antes dele ser igual ao n_2 da itenração passada, para após isso somar o n_2 da interação passada com o n_1 da interação passada
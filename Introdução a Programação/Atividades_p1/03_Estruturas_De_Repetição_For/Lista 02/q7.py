numero = int(input("Digite o número para a verificação: "))
validacao = True

if numero == 0 or numero == 1:
    print(f"o número {numero} não é primo!")
    print;
else:
    for i in range(2, numero):
        if (numero % i) == 0 and i != numero:
            validacao = False
            break
    if validacao: 
        print(f"o número {numero} é primo!")
    else:
        print(f"o número {numero} não é primo!")
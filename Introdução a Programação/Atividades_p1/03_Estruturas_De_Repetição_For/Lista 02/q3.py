n_pessoas = int(input("Digite a quantidade de pessoas: "))

total_pessoas = 0
for i in range (n_pessoas):
    total_pessoas += int(input(f"Digite a idade da pessoa {i+1}: "))

total_pessoas = total_pessoas/n_pessoas

if (total_pessoas <= 25):
    print("A turma é jovem!")
elif (total_pessoas > 25 and total_pessoas <= 60):
    print("A turma é adulta!")
else:
    print("A turma é idosa!")
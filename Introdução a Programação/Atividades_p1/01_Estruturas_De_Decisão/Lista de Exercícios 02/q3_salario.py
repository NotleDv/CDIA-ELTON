## Questão 03
# Autor: Elton de Assis
# Curso: Ciência de Dados e Inteligência Artifícial

horas_trabalha = float(input('Digite a quantidade de horas trabalhadas: '))
valor_horas = float(input('Digite o valor por hora trabalhada: '))

salario = horas_trabalha*valor_horas

# Calculos
imposto_renda = salario*0.11
inss = salario*0.08
sindicato = salario*0.05
salario_final = salario-(inss+sindicato+imposto_renda)

#Prints
print(f'Salário Bruto: R$ {salario}')
print(f'IR (11%): R$ {imposto_renda}')
print(f'INSS (8%): R$ {inss}')
print(f'Sindicato (5%): R$ {sindicato}')
print(f'Salário Liquido: R$ {salario_final}')

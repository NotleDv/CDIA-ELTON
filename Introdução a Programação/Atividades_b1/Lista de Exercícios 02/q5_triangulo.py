## Questão 05
# Autor: Elton de Assis
# Curso: Ciência de Dados e Inteligência Artifícial

lado_01 = float(input('Digite o primeiro lado do triângulo: '))
lado_02 = float(input('Digite o segundo lado do triângulo: '))
lado_03 = float(input('Digite o terceiro lado do triângulo: '))

if ((lado_01 == lado_02) and (lado_01 == lado_03) and (lado_02 == lado_03)):
    print('Triângulo Equilátero')
elif ((lado_01 != lado_02) and (lado_01 != lado_03) and (lado_02 != lado_03)):
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')
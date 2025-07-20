## Questão 06
# Autor: Elton de Assis
# Curso: Ciência de Dados e Inteligência Artifícial

nota_1 = float(input('Nota 01: '))
nota_2 = float(input('Nota 02: '))

media = (nota_1+nota_2)/2

if ((media > 9.0) and (media <= 10)):
    print('Conceito: A')
    
elif ((media > 7.5) and (media <= 9.0)):
    print('Conceito: B')
    
elif ((media > 6.0) and (media <= 7.5)):
    print('Conceito: C')
    
elif ((media > 4.0) and (media <= 6.0)):
    print('Conceito: D')
    
else:
    print('Conceito: E')
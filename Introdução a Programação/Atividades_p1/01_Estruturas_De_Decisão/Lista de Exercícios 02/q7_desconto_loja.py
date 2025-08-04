## Questão 07
# Autor: Elton de Assis
# Curso: Ciência de Dados e Inteligência Artifícial

valor = float(input('Valor do produto: '))
forma_pagamento = input('Forma de pagamento: ')

if ((valor >= 100) and (forma_pagamento == 'dinheiro')):
    print('R$', valor*0.9)
    
elif ((forma_pagamento != 'cheque') and (forma_pagamento != 'dinheiro')):
    print("Forma de pagamento inválida")
    
else:
    print('R$', valor)
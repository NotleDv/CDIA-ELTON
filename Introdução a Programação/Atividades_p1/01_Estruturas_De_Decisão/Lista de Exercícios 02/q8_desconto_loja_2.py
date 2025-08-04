## Questão 08
# Autor: Elton de Assis
# Curso: Ciência de Dados e Inteligência Artifícial

# Inputs -------------------------------------------------
valor = float(input('Valor do produto: '))
forma_pagamento = input('Forma de pagamento: ')

if (forma_pagamento == 'cartão'):
    funcao = input('Crédito ou Débito: ')
    
    if (funcao == 'crédito'):
        parcelas = int(input('Quantidade de parcelas: '))


# Condicionais -------------------------------------------
if ((valor >= 100) and (forma_pagamento == 'dinheiro')):
    print('R$', valor*0.9)

elif ((forma_pagamento != 'cheque') and (forma_pagamento != 'dinheiro') and (forma_pagamento != 'cartão')):
    print(f"Forma de pagamento inválida")

elif ((forma_pagamento == 'cartão') and (funcao == 'crédito')):
    print('R$', valor)
    print(f'{parcelas} parcelas de R$ {valor/parcelas}')
   
else:
    print('R$', valor)
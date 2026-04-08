# atividade 01 - Loja de informática.

valor_inicial_compra = float (input('Insira o valor total da compra:  '))
desconto_promocao = valor_inicial_compra * 0.16
# total_liquido_sem_desconto = valor_inicial_compra 
# total_liquido_com_desconto = valor_inicial_compra - desconto_promocao

# print (f'Total a pagar = {valor_inicial_compra}')

if valor_inicial_compra > 250.00:  
    print (f'Você recebeu desconto, o total a pagar: {valor_inicial_compra - desconto_promocao:.2f}.')
else:
    print (f'Total a pagar será = {valor_inicial_compra: .2f}')


 

# ------------------------------ correção atividade

valor = float (input('Informe o valor: '))

if valor>250:
    desconto = valor * 0.16
    valor_novo = valor - desconto
    print (f'O total a pagar é {valor_novo: .2f}')

else:
    print (f'O total a pagar é {valor: .2f}')


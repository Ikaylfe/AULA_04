valor_inicial = float (input('Insira o valor total da compra:  '))
tipo_pgto = (input ('Forma de pgto:')) .lower ()
if valor_inicial > 250.00 and tipo_pgto == "a vista":
    desconto = valor_inicial * 0.16  
    print (f'Total a pagar = {valor_inicial - desconto:.2f}.')
else:
    print (f'Total a pagar = {valor_inicial: .2f}')
    


# Estrutura if

idade = int(input ('insira sua idade:  '))

if idade >= 18:
    print ('Você é adulto')
else: # >>>>>>>>>>>>>>>>>> (else não recebe condições)
    print ('Você não é adulto')

# _____________________________________________

pontuacao = int( input('Insira sua pontuação:  '))

if pontuacao >=100:
    print('Você foi excelente!')

elif pontuacao >=50: # >>>>>>> ( pode incluir condição)
    print ('Você teve bom desempenho!') 
elif pontuacao >= 25:
    print ('Você teve uma pontuação satisfatória.')
else:
    print ('Pratique mais!') 

# --------------------------------

# Operadores and e or: AND
usuario =input('Nome:')
senha = input ('senha: ')
if usuario == "admin" and senha == "1234":
    print ('Login realizado com sucesso')
else :
    print('Senha ou usuário incorreto.')

# Operadores and e or: OR
usuario =input('Nome:')
senha = input ('senha: ')
if usuario == "admin" or senha == "1234":
    print ('Login realizado com sucesso')
else :
    print('Senha ou usuário incorreto.')


# .lower ()- letras minusculas
# .upper ()- letras maiusculas
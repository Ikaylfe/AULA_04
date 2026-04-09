# # Estrutura if

# idade = int(input ('insira sua idade:  '))

# if idade >= 18:
#     print ('Você é adulto')
# else: # >>>>>>>>>>>>>>>>>> (else não recebe condições)
#     print ('Você não é adulto')

# # _____________________________________________

# pontuacao = int( input('Insira sua pontuação:  '))

# if pontuacao >=100:
#     print('Você foi excelente!')

# elif pontuacao >=50: # >>>>>>> ( pode incluir condição)
#     print ('Você teve bom desempenho!') 
# elif pontuacao >= 25:
#     print ('Você teve uma pontuação satisfatória.')
# else:
#     print ('Pratique mais!') 

# # --------------------------------

# # Operadores and e or: AND
# usuario =input('Nome:')
# senha = input ('senha: ')
# if usuario == "admin" and senha == "1234":
#     print ('Login realizado com sucesso')
# else :
#     print('Senha ou usuário incorreto.')

# # Operadores and e or: OR
# usuario =input('Nome:')
# senha = input ('senha: ')
# if usuario == "admin" or senha == "1234":
#     print ('Login realizado com sucesso')
# else :
#     print('Senha ou usuário incorreto.')


# # .lower ()- letras minusculas
# # .upper ()- letras maiusculas

# # -------- Exemplos If's encadeado

# nota = 9

# if nota >= 9:
#     print('A')
# elif nota>=7:
#     print('B')
# elif nota>=5:
#     print('C')
# elif nota>=3:
#     print('D')

# else:
#     print('E') 

# # --- Exemplos If's não encadeado

# nota = 9

# if nota >= 9:
#     print('A')
# if nota>=7:
#     print('B')
# if nota>=5:
#     print('C')
# if nota>=3:
#     print('D')

# else:
#     print('E') 


# Exemplo If's aninhados

# nota=float(input('Insira a nota:'))
# frequencia=float(input('Informe a frequência:'))

# if nota>=7:
#     # Aprovado por nota, checar frequência.
#     if frequencia>=75:
#         print('Aprovado por nota e frequência.')
#     else:
#         print('Reprovado por frequência baixa.')
# else:
#     print('Reprovado por nota.')
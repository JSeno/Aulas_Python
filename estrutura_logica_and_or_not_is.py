"""
Estruturas lógicas and(e), or(ou), not(não), is(é)
Operadores unários:
    - not
Operadores binários:
    - and, or, is
Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido

"""

ativo = False
logado = False

# Se não estiver ativo faça isso:
#if not ativo:
   #print('Você precisa ativar sua conta. Por favor verifique seu e-mail')
#else:
    #print('Seja bem-vindo usuário')

#print(not False)

if ativo:
    print('Você precisa ativar sua conta. Por favor, verifique sua conta')
else:
    print('Seja bem-vindo usuário!')

print(ativo is True)

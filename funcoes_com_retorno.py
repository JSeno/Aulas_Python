"""
Funções com retorno

Obs: Não precisamos necessariamente criar uma variavel para receber o retorno de uma função. Podemos passar a execução
da função para outras funções.

Obs: Sobre a palavra return
1 - Ela finaliza a função, ou seja ela sai da execução da função;
2 - Podemos ter em uma função, diferentes returns;
3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores;
"""
# numeros = [1, 2, 3]
# ret_pop = numeros.pop()
# print(f'Retorno de pop: {ret_pop}')
# ret_pr = print(numeros)
# print(f'Retorno de print: {ret_pr}')

# Exemplo função

# def quadrado_de_7():
#     print(7 * 7)
#
# ret = quadrado_de_7()
# print(f'Retorno {ret}') # Não retorna nada já que o print imprimi na tela e não retorna

# Refatorar a função para ela retornar o valor
# def quadrado_de_7():
#     return(7 * 7)

# Foi criado uma variado para receber o retorno da função
# ret = quadrado_de_7()
# print(f'Retorno {ret}')

# Exemplo sem criar variável
# print(f'Retorno: {quadrado_de_7()}')

# def diz_oi():
#     return 'OI !'
#
# print(diz_oi())
#
# alguem = 'Pedro'
# print(diz_oi() + alguem)

# Exemplo 1
# def diz_oi():
#     print('Estou sendo executado antes do retorno') # Ela é executada já que está antes do retorno.
#     return 'oi'
#     print('Estou sendo executado após o retorno...') # Ela não será executada já que está após o return
#
# print(diz_oi())

# Exemplo 2
# def nova_funcao():
#     variavel = False
#     if variavel:
#         return 4
#     elif variavel is None:
#         return 3.2
#     return 'b'
#
# print(nova_funcao())

#
# def outra_funcao():
#     return 1, 2, 3, 4, 5
#
# num1, num2, num3, num4, num5 = outra_funcao()
# print(num1, num2, num3, num4, num5)
# print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

# from random import random
#
#
# def joga_moeda():
#     # Gera um número pseudo randomico entre 0 e 1
#     if random() > 0.5:
#         return 'Cara'
#     return 'Coroa'
#
# print(joga_moeda())
# help(random())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária

# def eh_impar():
#     numero = 12347
#     if numero % 2 != 0:
#         return 'É impar'
#     return 'É par' # É desnecessário colocar Else podemos dizer diretamente faça isso.

# print(eh_impar())
print('Hello World')
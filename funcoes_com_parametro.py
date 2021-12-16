"""
Funções com Parâmetros (de entrada)
- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""
# Refatorando uma função

# def quadrado(numero):
#     # return numero * numero
#     return numero ** 2

# print(quadrado(7))
# print(quadrado(2))
# print(quadrado(5))

# ret = quadrado(6)
# print(ret)

# Refatorando a função

# def cantar_parabens(aniversariante):
#     print('Parabéns para você')
#     print('Nesta data querida')
#     print('Muitas felicidades')
#     print(f'Viva a/o {aniversariante}')

# cantar_parabens('Patrícia')

# Funções podem ter n parâmetros de entrada, Ou seja podemos receber como entrada 
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo

# def soma(a, b): # a, b são parâmetros
#     return a + b

# def multiplica(num1, num2):
#     return num1 * num2

# def outa(num1, b, msg):
#     return (num1 + b) * msg


# print(soma(2, 5)) # 2, 5 são argumentos quando estão executando 
# print(soma(10, 20))
# print(multiplica(10, 5))
# print(outa(10, 9, "(-_-)"))

# Obs: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# Nomeando parâmetros

# def nome_completo(nome, sobrenome):
#     return f'seu nome completo é {nome} {sobrenome}'

# print(nome_completo('Angelina', 'Jolie'))

# A diferenças entre Parâmetros e Argumentos
# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa!!

# nome = 'Felicity'
# sobrenome = 'Jones'
# print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

# 

# Erro comum na utilização do return

# def soma_impares(numeros):
#     total = 0
#     for num in numeros:
#         if num % 2 !=0:
#             total = total + num
#     return total # Return finaliza a função, cuidado ao usar principalmente nos loops

# lista = [1, 2, 3, 4, 5, 6, 7]  # Funcionaria com tupla

# print(soma_impares(lista))
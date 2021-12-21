"""
Erros mais comuns em python
Atenção! é importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do código

Os erros mais comuns:
SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.
NameError -> Ocorre quando uma variável ou função não foi definida
TypeError -> Ocorre quando uma função / operação / ação é aplicada a um tipo errado.
IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.
ValueError -> Ocorre quando uma funçaõ ou operação built-in recebe um argumento com tipo correto mas valor inapropriado.
KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe
AttributeError -> Ocorre quando uma variável não tem um atributo/ função
IndentationError -> Ocorre quando não respeitamos a indentação do Python que são de 4 espaços.

Obs: Exceptions e Erros são sinônimos na programação
Obs: Importante ler e prestar atenção na saída de error.
"""
# Exemplos de SyntaxeError:
# def funcao: # Falta os parênteses após a função seria 'def funcao():' o correto
    # print('geek university')
# None = 1  # Palavra reservada do Python e atribuindo valor, você não pode utilizar palavras reservadas como nome de  variáveis.
# return # A palavra return deve ser colocada em uma função

# Exemplos de NameError
# print(geek) # O nome geek não foi definido como uma variável e nem atribuido como string
# geek() # Essa função não foi definida.
# a = 18
# if a < 10:
#     msg = 'é maior que 10'
# print(msg) # Como não foi definido o msg para quando a for maiior que 10 vira NameError

# Exemplos TypeError
# print(len(5)) # TypeError o objeto do tipo int não tem a função len
# print('geek' + []) # Não é possível concatenar uma string com uma lista estando vazia ou não., só é possível string + string

# Exemplos de IndexError
# lista = ['Geek']
# print(lista[2]) # A lista tem tamanho 1 que é o índece [0] não é possível acessar elementos que não existem.

# Exemplos de ValueError
# print(int('geek')) # O cast int espera receber como entrada uma string mas o valor não pode ser convertido para int
# print(float('geek'))

# Exemplos de KeyError
# dict = {'python': 'university'}
# print(dict['geek']) # Não existe no dicionário a chave geek

# Exemplos de AttributeError
# tupla = (11, 2, 31, 4)
# print(tupla.sort()) # A função .sort() pertence a lista e não tupla por isso vai gerar attributeerror.

# Exemplos de IndentationError
# def nova():
# print(geek) # Não foi respeitado os 4 espaços de indentation
# nova()
# for i in range(10):
# i + 1 # Novamente não foi respeitado a indentação
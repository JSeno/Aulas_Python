"""
Listas
Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferenças em seres DINÂMICO ou e
também podermos colocar QUALQUER tipo de dados.

Linguagens C/Java: arrays
    - Possuem tamanho e tipo de dado fixo; Ou seja nesstas linguagens se você criar um array do tipo int e com tamanho
    5, este arrua será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
    - Dinâmico: não possui tamanho fixo; Ou seja podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado; Não possuem tipo de dado fixo; Ou seja, poemos colocar qualquer tipo de dado;
As listas em python são representadas por colchetes: []

"""

#lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

#lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

#lista3 = []

#lista4 = list(range(11))

#lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
#if 8 in lista4:
    #print('Encontrei o número 8')
#else:
    #print('Não há número 8 na lista')

#if 'e' in lista5:
    #print('Encontrei a letra "e"')
#else:
    #print('Não encontrei a letra "e"')

#num = 7
#if num in lista4:
    #print(f'Encontrei o número {num}')
#else:
    #print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista:
#print(lista1, 'Antes de ser ordenada')
#lista1.sort()
#print(lista1, 'Após ser ordenada')

# Podemos facilmente contar o valor de uma lista
#print(lista1.count(1), 'Contando quantos números "1" tem na lista')
#print(lista5.count('e'), 'Contando quantas letras "e" tem na lista')

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append
Obs: Com o append, nós só conseguimos adicionar 1 elemento por vez
"""
#print(lista1, 'Sem o append')
#lista1.append(42)
#print(lista1, 'Com o append foi adicionado o número 42 ao final da lista com o .append(42)')
#lista1.append([8, 3, 1])
#print(lista1, 'Foi adicionado com o .append([8, 3, 1]) uma lista dentro de outra lista.')

#if [8, 3, 1] in lista1:
    #print('Encontrei a lista, foi procurado a lista dentro da lista e não os números delas')
#else:
    #print('Não encontrei a lista')

#print(lista1, 'Antes de adicionar elementos dentro da lista')
#lista1.extend([123, 44, 67])
#print(lista1, 'Foi adicionados mais elementos dentro da lista no fim dela como .extend([123, 44, 67])')

# Podemos inserir um novo elemento na lista informando a posição do índice.
# Obs: Não foi substituido o valor ínicial o valor foi deslocado para direita.

#print(lista1, 'Antes de usar o .insert()')
#lista1.insert(2, 'Novo valor após usar o .insert(2, "Novo valor")')
#print(lista1)

# Podemos facilmente juntar duas listas
#print(lista1)
#print(lista2)
#lista6 = lista1 + lista2
#print(lista6, 'Foi criado uma nova lista concatenando lista1 + lista 2')
#lista1.extend(lista2)
#print(lista1, 'Aqui foi usado o .extend("lista2")')

# Utilizando o reverse
#lista1.reverse()
#lista2.reverse()
#print(lista1, 'Revertemos a lista utilizando o .reverse()')
#print(lista2, 'Revertemos a lista utilizando o . reverse()')

#print(lista1[::-1])
#print(lista2[::-1])

# Copiar uma lista
#lista6 = lista2.copy()
#print(lista6, 'a lista foi copiada com o .copy()')

# Saber quantos elementos tem na lista
#print(len(lista2), 'O comando len retorna quantos elementos tem na lista')

# Podemos remover facilmente o último elemento de uma lista
#print(lista5)
#lista5.pop()
#print(lista5, 'Foi removido o último elemento com o comando .pop()')

# Podemos remover um elemento pelo índice
#print(lista5)
#lista5.pop(2)
#print(lista5, 'Foi removido o elemento no índice 2 com o .pop(2) e os elementos a direita foram deslocados a esquerda')

# Podemos remover todos elementos
#print(lista5)
#lista5.clear()
#print(lista5, 'Com o comando .clear() a lista foi completamente limpa')
#curso = 'Programação em Python: Essencial '
#print(curso, '|  Antes do uso do .split()')
#curso = curso.split()
#print(curso, '|  Após o uso do .split()')

# Convertendo uma lista em uma string
#lista6 = ['Programação', 'em', 'Python', 'Essencial']
#print(lista6)

#curso = ' '.join(lista6)
#print(curso, '|  Uso do .join()')
#curso = '`\(-.-)/´'.join(lista6)
#print(curso)

# Exemplo 1 utilizando for
#soma = 0
#for elemento in lista2:
    #print(elemento)
   # soma = soma + elemento
#print(soma)

# Exemplo 2 utilizando while
#carrinho = []
#produto = ''
#while produto != 'sair':
    #print("Adicione um produto na lista ou digite 'sair' para sair: ")
   # produto = input()
    #if produto != 'sair':
        #carrinho.append(produto)

#for produto in carrinho:
    #print(produto)

# Utilizar variáveis em listas
#numeros = [1, 2, 3, 4, 5]
#print(numeros)
#num1 = 1
#num2 = 2
#num3 = 3
#num4 = 4
#num5 = 5
#numeros = [num1, num2, num3, num4, num5]
#print(numeros)

# Fazemos acesso aos elementos de forma indexada
#cores = ['verde', 'amarelo', 'azul', 'branco']
#print(cores[0])
#print(cores[1])
#print(cores[2])
#print(cores[3])

# Fazer acesso aos elementos de forma indexada reversa
#print(cores[-1])
#print(cores[-2])
#print(cores[-3])
#print(cores[-4])
#for cor in cores:
    #print(cor)

#indice = 0
#while indice < len(cores):
    #print(cores[indice])
    #indice = indice + 1

#for indice, cor in enumerate(cores):
    #print(indice, cor)

#lista = []
#lista.append(42)
#lista.append(42)
#lista.append(33)
#lista.append(33)
#lista.append(42)
#print(lista)
# Outros métodos não tão importantes mas também úteis
# Encontrar o índice de um elemento na lista
#numeros = [5, 6, 7, 8, 9, 10]
#print(numeros.index(6), 'Em qual índice está o valor 6')
#print(numeros.index(9), 'Em qual índice está o valor 9')
# Obs: Caso não tenha o elemento na lista será apresentado erro
# Podemos azer busca dentro de um range ou seja, qual indice começar a buscar
#numeros = [5, 6, 7, 8, 9, 10]
#print(numeros.index(5, 1, 4)) # Buscando a partir do índice 1
#print(numeros.index(5, 2, 2)) # buscando a partir do índice 2
#print(numeros.index(5, 3, 3)) # buscando a partir do índice 3

# Revisão de slicing
# lista(inicio:fim:passo)
# range(inicio:fim:passo)
# Trabalhando com slice de lista com o parâmetro 'inicio'

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(lista[1:]) # Iniciando no índice 1 e pegando todos os relementos restantes
#print(lista[::]) # Pega todos os elementos
#print(lista[1::2]) # Começa em 1 vai até o final, de 2 em 2
#print(lista[::2]) # Começa em 0 vai até o final, de 2 em 2
#print(lista[1::-1]) # Lista invertida

#nome = 'Programação em Python Essencial'
#print(nome)
#print(nome[::-1])

# Invertendo valores em uma lista
#nomes = ['Geek', 'University']
#print(nomes)
#nomes[0], nomes[1] = nomes[1], nomes[0]
#print(nomes)
#nomes.reverse()
#print(nomes)

# Soma, valor máximo,, valor mínimo, tamanho
# Se os valores forem todos inteiros ou reais.

#lista = [1, 2, 3, 4, 5, 6]
#print(sum(lista))

# Compiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1
# lista = [1, 2, 3]
# print(lista)
# nova = lista.copy()
# print(nova)
#
# nova.append(4)
#
# print(lista)
# print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram
#totalmente idependentes, ou seja , modificando uma lista, não afeta a outra. Isso em Python
#é chamado de Deep Copy(copia profunda)
# Forma 2
# lista = [1, 2, 3]
# print(lista)
# nova = lista #copia
# print(nova)
# nova.append(4)
# print(lista)
# print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar modificação
# em uma das listas, essa modificação refletiu em ambas as listas.
# Isso em python é chamado de shallow copy.
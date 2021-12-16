"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.
- Aqui no Python, os conjuntos são chamados de Sets.
Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação
deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.
Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
- Um dicionário tem chave/valor;
- Um conjunto tem apenas valor;

"""
# Definindo um conjunto:
# Forma 1
# s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.
# print(s)
# print(type(s))
# # Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e
# # não fará parte do conjunto.
#
# # Forma 2 - Mais comum
# s = {1, 2, 3, 4, 5, 5}
# print(s)
# print(type(s))
#
# # Podemos verificar se determinado elemento está contido no conjunto
# if 3 in s:
#     print('Tem o 3')
# else:
#     print('Não tem o 3')

# Importante lembar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados então temos 10 elementos.
# lista = [99, 2, 2, 34, 34, 23, 12, 1, 44, 5]
# print(f'Lista: {lista} com {len(lista)} elementos')
#
# # Tuplas aceitam valores duplicados então temos 10 elementos.
# tupla = (99, 2, 2, 34, 34, 23, 12, 1, 44, 5)
# print(f'Tupla: {tupla} com {len(tupla)} elementos')
#
# # Dicionários não aceitam chaves duplicados então temos 8 elementos.
# dicionario = {}.fromkeys([99, 2, 2, 34, 34, 23, 12, 1, 44, 5], 'dict')
# print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
#
# # Conjuntos não aceitam valores duplicados então temos 8 elementos.
# conjunto = {99, 2, 2, 34, 34, 23, 12, 1, 44, 5}
# print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em sets.

# s = {1, 'b', True, 34, 22, 44}
# print(s)
# print(type(s))
#
# Podemos iteirar em um set normalmente
# for valor in s:
#     print(valor)

# Usos interessantes com Sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira e museu e os visitantes informam manualmente
# a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python, já que uma lista podemos adicionar novos elementos e ter repetição.

# cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
# print(cidades)
# print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja únicas temos.
# O que você faria?
# Podemos utilizar o set para isso
# print(len(set(cidades)))

# Adicionando elementos em um conjunto
# s = {1, 2, 3}
# s.add(4)
# print(s)

# Remover elementos em um conjunto
# s = {1, 2, 3}
# print(s)
# Forma 1
# s.remove(3) # Não é índice e sim o valor a ser removido
# print(s)
# Obs: caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2
# s.discard(2)
# print(s)
# Obs: Se o valor não for encontrado nenhum erro é gerado.

# Copiando um conjunto para outro
# s = {1, 2, 3}
# print(s)

# Forma 1 - Deep Copy
# novo = s.copy()
# print(novo)
# novo.add(4)
# print(novo)
# print(s)

# Forma 2 - Shallow Copy
# s = {1, 2, 3}
# novo = s
# novo.add(4)
# print(novo)
# print(s)

# Podemos remover todos os itens de um conjunto
# s = {1, 2, 3}
# print(s)
# s.clear()
# print(s)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos um contendo estudantes do curso python e um contendo estudantes de java
# estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
# estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
#
# # Veja que alguns alunos que estudam python também estudam java.
# # Precisamos gerar um conjunto com nomes de estudantes únicos
#
# # Forma 1 - Utilizando union
# unicos1 = estudantes_python.union(estudantes_java)
# print(unicos1)
#
# # Forma 2 - Utilizando o caractere pip |
# unicos2 = estudantes_python | estudantes_java
# print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - utlizando intersection
# ambos1 = estudantes_python.intersection(estudantes_java)
# print(ambos1)

# Forma 2 - Utilizando &
# ambos2 = estudantes_python & estudantes_java
# print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

# so_python = estudantes_python.difference(estudantes_java)
# print(so_python)
#
# so_java = estudantes_java.difference(estudantes_python)
# print(so_java)

# Soma, valor máximo, valor mínimo, tamanho
# Se os valores forem todos inteiros e reais
# s = {1, 2, 3, 4, 5, 6}
# print(sum(s))
# print(max(s))
# print(min(s))
# print(len(s))
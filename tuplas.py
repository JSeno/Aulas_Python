# tupla = ('Geek University', 'Programação em Python Essencial')
# escola, curso = tupla
#
# print(escola)
# print(curso)

# Métodos para: adição e remoção de elemetnos nas tuplas não existe, dado o fato das tuplas serem imutaveis.

# Soma*, valor máximo, valor mínimo e Tamanho
# Se os valores forem iteiros ou reais
# tupla = (1, 2, 3, 4, 5, 6)
# print(sum(tupla))
# print(max(tupla))
# print(min(tupla))
# print(len(tupla))

# Concatenação em tuplas
# tupla1 = (1, 2, 3)
# print(tupla1)
#
# tupla2 = (4, 5, 6)
# print(tupla2)
#
# print(tupla1 + tupla2) # Tuplas são imutáveis
# print(tupla1)
# print((tupla2))
#
# tupla3 = tupla1 + tupla2
# print(tupla3)
# print(tupla1)
# print(tupla2)
#
# tupla1 = tupla1 + tupla2 # Tuplas são imutáveis mas podemos sobreescrever seus valores
# print(tupla1)

# Verificar se determinado elemento está contida na tupla
# tupla = (1, 2, 3)
# print(3 in tupla) # Retorna valor boleano

# Inteirando sobre uma tupla
# tupla = (1, 2, 3)
# for n in tupla:
#     print(n)
#
# for indice, valor in enumerate(tupla):
#     print(indice, valor)

# Contando elementos dentro de uma tupla
# tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
# print(tupla.count('c'))
#
# escola = tuple('Geek University')
# print(escola)
#
# print(escola.count('e'))

# Dicas para utilização de tuplas
# Devemos utilizar tuplas sempre que não precisamor modificar os dados contidos em uma coleção
# Exemplo 1
# meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
# 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
# # print(meses)
# # O Acesso a elementos de uma tupla também é semelhante a de uma lista
# # print(meses[5])
# #
# # # Interar com while
# # i = 0
# # while i < len(meses):
# #     i = i +1
#
# # Verificamos em qual indice um elemento está na tupla
# # print(meses.index('Junho'))
# # Obs: Caso o elemento não exista, será gerado ValueError.
#
# # Slicing
# # tupla(inicio:fim:passo)
# print(meses[5:9])

# Por quê utilizar tuplas?
# Tuplas são mais rápidas do que listas.
# Tuplas deixam seu código seguro
# Isso porque trabalhar com elementos imutáveis traz segurança para seu código

# # Copiando uma tupla para outra
# tupla = (1, 2, 3)
# print(tupla)
# nova = tupla # Na tupla não temos o problema de shallo copy
# print(nova)
# print(tupla)
# outra = (4, 5, 6)
# nova = nova + outra
# print(nova)
# print(tupla)

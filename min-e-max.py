"""
Min e Max

max() -> Retorna o maior valor em um interável ou o maior de dois ou mais elementos.
min() -> Retorn a o menor valor em um iterável ou o menor de dois ou mais elementos
"""

# Exemplo
# lista = [1, 8, 4, 99, 34, 129]
# print(max(lista))

# tupla = (1, 8, 4, 99, 34, 129)
# print(max(tupla))

# conjunto = {1, 8, 4, 99, 34, 129}
# print(max(conjunto))

# dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
# print(max(dicionario))
# print(max(dicionario.values()))

# # Faça um programa que receba dois valores do usuário e mostre o maior
# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))
# print(max(val1, val2))

# print(max(4, 67, 54))
# print(max('a', 'b', 'c', 'g'))
# print(max(3.145, 5.789))
# print(max('Geek University'))

# Exemplo
# lista = [1, 8, 4, 99, 34, 129]
# print(min(lista))

# tupla = (1, 8, 4, 99, 34, 129)
# print(min(tupla))

# conjunto = {1, 8, 4, 99, 34, 129}
# print(min(conjunto))

# dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
# print(min(dicionario))
# print(min(dicionario.values()))

# # Faça um programa que receba dois valores do usuário e mostre o maior
# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))
# print(min(val1, val2))

# print(min(4, 67, 54))
# print(min('a', 'b', 'c', 'g'))
# print(min(3.145, 5.789))
# print(min('Geek University'))

# Outros exemplos
# nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# print(max(nomes)) # Tim, ele leva em conta a ordem alfabética
# print(min(nomes)) # Arya ele leva em conta a ordem alfabética

# print(max(nomes, key=lambda nome: len(nome))) # Ollivander
# print(min(nomes, key=lambda nome: len(nome))) # Tim

musicas = [
    {'titulo': 'ThunderStruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': "Too old to rock'in'roll', too young to die", 'tocou': 32},
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# desafio! Imprima somente o título da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# desafio! Como encontrar a música mais tocada e menos tocada sem usar max(), min(), lambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']


for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

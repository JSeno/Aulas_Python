"""
Sorted

Obs: Não confunda apesar de seu nome com a função sort() que já estudamos em listas. O sort() só funciona em listas.
Podemos utilizar o sorted() com qualquer iterável.
Como o próprio nome diz, sorted() serve para ordenar.

Obs: O sorted() sempre retorna uma lista com os elementos do iterável ordenados
"""

# Exemplo 
# numeros = [6, 1, 8, 2]
# print(numeros)
# # print(sorted(numeros)) # Ordenar do menor para o maior
# # print(numeros)

# # Adicionando parâmetros ao sorted()

# print(sorted(numeros))
# print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted() para coisas mais complexas

# usuarios = [
#     {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
#     {'username': 'carla', 'tweets': ['Eu amo meu gato']},
#     {'username': 'jeff', 'tweets': []},
#     {'username': 'bob123', 'tweets': []},
#     {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
#     {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'},
#     ]

# print(usuarios)
# # Ordenando pelo username - Ordem Alfabética
# print(sorted(usuarios, key=lambda usuario: usuario['username']))
# print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

# # Ordenando pelo números de tweets
# print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

# Ultimo de exemplo
musicas = [
    {'titulo': 'ThunderStruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': "Too old to rock'in'roll', too young to die", 'tocou': 3},
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
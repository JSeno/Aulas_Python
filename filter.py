"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

"""
# valores = 1, 2, 3, 4, 5, 6
# media = sum(valores) / len(valores)
# print(media)

# Biblioteca para trabalhar com dados estatisticos
# import statistics


# # Dados coletados de algum sensor
# dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# # Calculando a média dos dados utilizando a função mean()
# media = statistics.mean(dados)
# print(f'Média: {media}')

# # Obs: Assim como a função map(), a filter recebe dois parâmetros, sendo uma
# # função e um interável.

# res = filter(lambda x: x > media, dados)
# print(list(res))
# print(type(res))
# print(f'Novamente: {list(res)} os dados sumiram')
# # Obs: Após ser utilizado os dados de filter() os dados somem da memória

# paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
# print(paises)

# res = filter(None, paises)
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
# print(list(res))

# A diferença entre map() e filter() é:
# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada
# elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um interável e retorna um objeto filtrando apenas os elementos
# de acordo com a função.

# # Exemplo mais complexo
# usuarios = [
#     {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
#     {'username': 'carla', 'tweets': ['Eu amo meu gato']},
#     {'username': 'jeff', 'tweets': []},
#     {'username': 'bob123', 'tweets': []},
#     {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
#     {'username': 'gal', 'tweets': []},
#     ]

# # Filtrar os usuários que estão inativos no Twitter
# print(usuarios)

# inativos = list(filter(lambda usuario: len(usuario['tweets']) != 0, usuarios))
# print(inativos)

# # Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
# print('Forma 1:', inativos)

# # Forma 2
# inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
# print('Forma 2:', inativos)

# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo: 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é a {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
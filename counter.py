"""
Módulo ollections - Counter (Contador)
Collections -> High-performace Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo colections counter, que é parececido com um
dicionário. Contendo como chave o elemento da lista como parâmetro e como o valor a quantidade de ocorrências desse
elemento.

"""
# Utilizando o Counter

# Realizando o Import do Counter
from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer inteirável, aqui usamos uma lista
# lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5,3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
# res = Counter(lista)
# print(type(res))
# print(res)
# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.
 # Exemplo 2
# print(Counter('Geek University'))

# Exemplo 3
texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen 
book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and 
more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)
# Encontrando as 10 palavras com mais ocorrências no texto
print(res.most_common(10))

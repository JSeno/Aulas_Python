"""
Set Comprehension

lista = [1, 2, 3, 4]
set = {1, 2, 3, 4}
"""

# Exemplos
from typing import Counter


numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionário ao invès de set
numeros = {x:x ** 2 for x in range(10)}
print(numeros)

letras = {letra for letra in 'Geek University'}
print(letras)
print(len(letras))
print(Counter(letras))
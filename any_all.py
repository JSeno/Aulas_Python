"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""
# Exemplo all()
print(all([0, 1, 2, 3, 4])) # Todos os número são verdadeiros? O 0 é False então a função retornará False.
print(all([1, 2, 3, 4])) # Aqui os retornará True já que todos os elementos são True
print(all([])) # Retornará True já que o iterável está vazio

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina'] # Retornará True

print(all([nome[0] == 'C' for nome in nomes]))


# Obs: Um interável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, []])) # False

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

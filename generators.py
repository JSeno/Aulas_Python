"""
generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension... porque elas se chamam generators

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
"""

# Poderiamos ter feito utilizando Generator


# nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
# print(any(nome[0] == 'C' for nome in nomes))

# # list Comprehension
# res = [nome[0] == 'C' for nome in nomes]
# print(type(res))
# print(res)

# res = (nome[0] == 'C' for nome in nomes)
# print(type(res))
# print(res)


# Qual é a utilidade de getsizeof? Retorna a quantidade de bits em memória do elemento passado como parâmetro
from sys import getsizeof

# print(getsizeof('geek'))
# print(getsizeof('university'))
# print(getsizeof(12))
# print(getsizeof(1124))
# print(getsizeof(15134111634))
# print(getsizeof(False))

# Gerando uma lista de números com List Comprehension
# list_comp = getsizeof([x * 10 for x in range(1000)])

# # Gerando uma lista de números com List Comprehension
# set_comp = getsizeof({x * 10 for x in range(1000)})

# # Gerando uma lista de números com List Comprehension
# dic_comp = getsizeof({x:x * 10 for x in range(1000)})

# # Gerando uma lista de números com Generator
# gen = getsizeof(x * 10 for x in range(1000))

# print('Para fazer a mesma tarefa gastamos em memória: ')
# print(f'List Comprehension: {list_comp} bytes')
# print(f'Set Comprehension: {set_comp} bytes')
# print(f'Dictionary Comprehension: {dic_comp} bytes')
# print(f'Generator Comprehension: {gen} bytes')

# Eu posso interar no Generator Expression? SIm
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
    
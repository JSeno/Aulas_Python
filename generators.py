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


nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))
"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performace.

"""
# Fazendo o import
from collections import deque

deq = deque('geek')
print(deq)

# Adicionando elemento no deque
deq.append('q')
print(deq)

deq.appendleft('k')
print(deq)

# Removendo elementos
print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)
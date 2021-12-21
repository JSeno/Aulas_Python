"""
Len, Abs, Sum, Round

#Len
len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.
#Abs
abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
# Sum
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos,
incluindo o valor inicial.
# Obs: O valor inicial é 0
# Round
round() - > Retorna um número arrendodado para n digíto de precisão após a casa decimal,
Se a precisão não for retornada retorna o inteiro mais próximo da entrada.

"""
# print(len('Geek University'))
# print(len([1, 2, 3, 4, 5]))
# print(len((1, 2, 3, 4, 5)))
# print(len({1, 2, 3, 4, 5}))
# print(len({'a':1, 'b':2, 'c':3, 'd':4, 'e':5}))

# print(len(range(0, 10)))

# # Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
# print('Geek University'.__len__())

# Exemplo de Abs
# print(abs(-5))
# print(abs(5))
# print(abs(3.14))
# print(abs(-3.14))

# Exemplos Sum
# print(sum([1, 2, 3, 4, 5]))
# print(sum([1, 2, 3, 4, 5], -5))

# print(sum([3.145, 5.678]))
# print(sum((1, 2, 3, 4, 5)))
# print(sum({1, 2, 3, 4, 5}))
# print(sum({'a':1, 'b':2, 'c':3, 'd':4, 'e':5}.values()))
# print(sum('Geek University', 'x'))

# Exemplos Round
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.212121212121, 2))
print(round(1.21999999, 2))
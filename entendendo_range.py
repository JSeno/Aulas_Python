"""
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com os loops for.
Ranges são utilizados para gerar sequências númericas, não de forma aleatória mas de sim de maneira especificada.
Formas gerias:
range(valor_de_parada)

Obs: valor_de_parada não incusive(inicio padrão 0, e passo de 1 em 1)

# Forma 1
for num in range(11):
    print(num)

# Forma 2
range(valor de inicio, valor de parada)

# Exemplo forma 2
for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
# Exemplo de forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4 (forma inversa)
range(valor_de_inicio, valor_de_parada, passo)

# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)

lista = list(range(10))
print(lista)

"""

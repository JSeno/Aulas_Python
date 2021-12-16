"""
Funções com Parâmetro Padrão (default paramters)
- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado():
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

"""

# def exponencial(numero, potencia = 2):
#     return numero ** potencia

# print(exponencial(2, 3))  # 2 * 2 * 2 = 8
# print(exponencial(3, 2))  # 3 * 3 = 9

# print(exponencial(3)) # Por padrão eleve ao quadrado
# print(exponencial(3, 5)) # Eleva a potencia informada pelo usuário


# Obs: Se o usuário passar somente 1 parâmetro, este será atribuido ao parâmetro número, e será calculado
# o quadrado deste número.
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro número e o segundo ao parâmetro potência, Então
# será calculada esta potência.

# Obs: Em funções python, os parâmetros com valores default (padrão) DEVEM sempre estár ao final da declaração
# ERRO!
# def teste(num=2, potencia):
#     return num ** potencia

# print(teste(6))

# # CORRETO!
# def teste(potencia, num=2):
#     return num ** potencia	

# print(teste(6))

# def soma(num1, num2):
#     return num1 + num2

# print(soma(4, 3))
# print(soma(4)) # TypeError
# print(soma())  # TypeError

# def soma(num1=10, num2=10):
#     return num1 + num2

# print(soma(4, 3))
# print(soma(4)) # Não apresenta mais TypeError
# print(soma())  # Não apresenta mais TypeError

# def mostra_informacao(nome='Geek', instrutor=False):
#     if nome == 'Geek' and instrutor:
#         return 'Bem-vindo Instrutor Geek'
#     elif nome == 'Geek':
#         return 'Eu pensei que você era o instrutor'
#     return f'Olá {nome}'

# print(mostra_informacao())
# print(mostra_informacao(instrutor=True)) # True
# print(mostra_informacao(True)) # True virou argumento nome
# print(mostra_informacao('Ozzy'))
# print(mostra_informacao(nome='Stephany'))

# Por quê utilizar parâmetros com valores default?
# - Nos permite ser mais flexiveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legiveis de código.

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
# - Qualquer tipo de dado:
# - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Exemplos
# def soma(num1, num2):
#     return num1 + num2


# def mat(num1, num2, fun=soma):
#     return fun(num1, num2)


# def subtracao(num1, num2):
#     return num1 - num2


# print(mat(2, 3))
# print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...
# Variáveis globais
# Variáveis locais

# instrutor = 'Geek'  # Variável global

# def diz_oi():
#     instrutor = 'Python' # Variável local
#     return f'Oi {instrutor}'

# print(diz_oi())

# Obs: Se tivermos uma variável local com o mesmo nome de uma variável global a local terá a preferência.

# def diz_oi():
#     prof = 'Geek' # Variável local
#     return f'Olá {prof}'

# print(diz_oi())
# print(prof) # NameError ela só é reconhecida dentro da função

# ATENÇÃO com variáveis globais, (se puder evitar, as evite)

# total = 0
# def incrementa():
#     total = total + 1  # UnboundLocalError - a variável local está sendo utilizada para processamento sem ter sido inicializada.
#     return total
# print(incrementa())

# total = 0
# def incrementa():
#     global total  # Estamos avisando que iremos utilizar a variável global
#     total = total + 1
#     return total
# print(incrementa())
# print(incrementa())
# print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

# def fora():
#     contador = 0
#     def dentro():
#         nonlocal contador # Não é local e nem global, é a variável que está dentro de uma função anterior
#         contador = contador + 1
#         return contador
#     return dentro()
# print(fora())
# print(fora())
# print(dentro()) # NameError ela é só conhecida dentro da função fora
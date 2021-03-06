"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java
for9int i = 0; i <10; i++){
    //execução do loop
}

Python
for item in interável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'Seu nome'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 interando sobre uma string
for letra in nome:
    print(letra)

# Exemplo de for 2 interando sobre uma string
for numero in lista:
    print(numero)

# range(valor inicial, valor final)
#Obs: O valor final não é incluso, sempre um a menos.

 
# Exemplo de for 3 interando sobre um range
for numero in range(1, 10):
    print(numero)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista


Enumerate:
((0, 'G')), ((1, 'e')), ((2, 'e')), ((3, 'k')) e assim por diante.

for indice,letra in enumerate(nome):
    print(nome[indice])
for indice, letra in enumerate(nome):
    print(letra)
for _, letra in enumerate(nome): # Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
    print(letra)
for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

# https://apps.timwhitlock.info/emoji/tables/unicode


# Original U+1F60D
# Modificado U0001F60D
emoji = 'U0001F60D'

for _ in range(3):
    for num in range(1, 11):    
        print('\U0001F60D' * num)

"""
nome = 'Geek University'
for letra in nome:
    print(letra, end='')



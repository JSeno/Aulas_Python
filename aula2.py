numero1 = input('Digite um número: ')
numero1 = int(numero1)

numero2 = input('Digite um número: ')
numero2 = int(numero2)

if(numero1==numero2):
    print('O número %d é igual a %d ' %(numero1, numero2))
if(numero1!=numero2):
    print('O número %d é diferente de %d ' %(numero1, numero2))
if(numero1<numero2):
    print('O número %d é menor que o %d ' %(numero1, numero2)) 
if(numero1>numero2):
    print('O número %d é maior que o %d ' %(numero1, numero2))
if(numero1>=numero2):
    print('O número %d é maior ou igual a %d ' %(numero1, numero2))
if(numero1<=numero2):
    print('O número %d é menor ou igual a %d ' %(numero1, numero2))
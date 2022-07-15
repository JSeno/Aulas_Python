"""

Try / Except / Else / Finally
Dica de quando e onde tratar código:
TODA ENTRADA DEVE SER TRATADA!

"""
# num = 0

# try:
#     num = int(input('informe um número: '))
# except ValueError:
#     print('Você não informou um número!')
# # O else só será executado se não ocorrer erro
# else:
#     print(f'Você digitou {num}')


# Finally
# try:
#     num = int(input('informe um número: '))
# except ValueError:
#     print('Você não informou um número!')
# else:
#     print(f'Você digitou {num}')
# O bloco finally sempre será executado independentemente de erro ocorra ou não
# finally:
#     print('Executando o finally')

# O finally também pode ser utilizado para fechar conexões com banco de dados ou desalocar recursos.

# def dividir(a, b):
#     return a /b

# num1 = int(input('informe o primeiro número: '))
# try:
#     num2 = int(input('informe o segundo número: '))
# except ValueError:
#     print('O valor precisa ser númerico')

# try:
#     print(dividir(num1, num2))
# except NameError:
#     print('Valor incorreto')

# def dividir(a, b):
#     try:
#         return int(a) / int(b)
#     except ValueError:
#         print('Valor incorreto')
#     except ZeroDivisionError:
#         return 'Não é possível dividir por zero'

# num1 = int(input('informe o primeiro número: '))
# num2 = int(input('informe o segundo número: '))
# print(dividir(num1, num2))

# def dividir(a, b):
#     try:
#         return int(a) / int(b)
#     except:
#         return "Ocorreu um erro"

# num1 = int(input('informe o primeiro número: '))
# num2 = int(input('informe o segundo número: '))
# print(dividir(num1, num2))

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ZeroDivisionError, ValueError):
        return "Ocorreu um erro"
        

num1 = int(input('informe o primeiro número: '))
num2 = int(input('informe o segundo número: '))
print(dividir(num1, num2))

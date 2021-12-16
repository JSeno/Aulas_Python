"""
Documentando funções com Docstrings

Obs: Podemos ter acesso á documentação de uma função em python utilizando o método especial __doc__

Podemos ainda fazer acesso á documentação com a função help()
"""

# def diz_oi():
#     """Uma função simples que retorna a string 'Oi' """
#     return 'Oi'

# print(diz_oi())
# print(help(diz_oi))
# print(diz_oi.__doc__)

# print(print.__doc__)

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou o 'número' á potencia informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2
    :return: retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

print(exponencial.__doc__)

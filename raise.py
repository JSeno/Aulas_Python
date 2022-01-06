"""
Levantando os próprios erros com raise

raise -> Lança exeções 
Obs: Não é uma função, é uma plavra reservada assim como def ou qualquer outra em python.
Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.
A forma geral de utilização é:

raise TipoDoErro('Menagem de erro')


# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', '7')

# Exemplo refatorado

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'preto')

Obs: O raise assim como return finaliza uma fução, ou seja nada após o raise é executado
"""


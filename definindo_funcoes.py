"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muito uteis para executrar procedimentos similares por repetidas vezes;

Obs: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplicada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- E muitas outras;
"""

# Exemplo de utilização de funções:
# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do Python print()
# print(cores)

# cores.append('roxo')
# print(cores)

# cores.clear()
# print(cores)

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.
# Mas então, como definir funções?
"""
Em python a forma geral de definir uma função é:
def nome_da_função(parâmetro_de_entrada):
    bloco_da_função
    
Onde:
nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline(snake case);
parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função de implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

Obs: veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em python para definir
blocos.
"""

# Definindo a primeira função
# Definição
def diz_oi():
    print('Oi!')

"""
Obs: 
1 - Veja que dentro de nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""
# Utilizando funções
# Chamada de execução
diz_oi()

"""
ATENÇÃO
"""
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

canta = cantar_parabens
canta()
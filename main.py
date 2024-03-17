'''Alunos: Ana Paula Borowsky de Borba e Anthony Sutil de Oliveira
ENUNCIADO
Criar um programa, utilizando que, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados. O programa irá receber 
como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias 
operações. Estas operações e dados estarão representadas em um arquivo de textos contendo 
apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra 
fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operação (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
O programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresentada acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos. Para que o programa possa ser testado você deve criar, no mínimo, 
três arquivos de entrada contendo um número diferente de operações, operações com dados diferentes, e 
operações em ordens diferentes. Os arquivos de entrada criados para os testes devem estar disponíveis 
tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor irá testar seu programa com 
os arquivos de testes que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor.'''

import sys

def executaOperacao(operacao, conjuntoA, conjuntoB):
    match (operacao):
        case "U":
            resultado = conjuntoA + conjuntoB
            print("União: conjunto 1 " + str(set(conjuntoA)).replace("'","") + ", conjunto 2 " + str(set(conjuntoB)).replace("'","") + ". Resultado: " + str(set(resultado)).replace("'","") + "\n")
        case "I":
            resultado = set(conjuntoA) & set(conjuntoB)
            print("Interseção: conjunto 1 " + str(set(conjuntoA)).replace("'","") + ", conjunto 2 " + str(set(conjuntoB)).replace("'","") + ". Resultado: " + str(set(resultado)).replace("'","") + "\n")
        case "C":
            resultado = [(a, b) for a in conjuntoA for b in conjuntoB]
            print("Produto Cartesiano: conjunto 1 " + str(set(conjuntoA)).replace("'","") + ", conjunto 2 " + str(set(conjuntoB)).replace("'","") + ". Resultado: " + str(set(resultado)).replace("'","") + "\n")
        case "D":
            resultado = set(conjuntoA) - set(conjuntoB)
            print("Diferença: conjunto 1 " + str(set(conjuntoA)).replace("'","") + ", conjunto 2 " + str(set(conjuntoB)).replace("'","") + ". Resultado: " + str(set(resultado)).replace("'","") +"\n")
        case _: 
            print("Opção desconhecida.")

def argumentosValidos(operacao, conjuntoA, conjuntoB):
    if operacao[0] == '' or conjuntoA[0] == '' or conjuntoB[0] == '':
        return False
    else:
        return True

nome_arquivo = (sys.argv[1])

with open(nome_arquivo, 'r') as arquivo:
    num_operacoes = int(arquivo.readline())
    for i in range(0, num_operacoes):
        operacao = arquivo.readline().strip().upper()
        conjuntoA = arquivo.readline().strip().replace(' ', '').split(',')
        conjuntoB = arquivo.readline().strip().replace(' ', '').split(',')

        if argumentosValidos(operacao, conjuntoA, conjuntoB):
            executaOperacao(operacao, conjuntoA, conjuntoB)
        else:
            print("Erro de formatação do arquivo. Possíveis erros: número de operações maior do que a quantidade de operações presentes no arquivo; um dos conjuntos não existe para completar a operação. Por favor verifique os detalhes no readme.")
            break
## Introdução

Trabalho da disciplina Resolução de Problemas de Natureza Discreta, do segundo período do curso de Ciência da Computação,
sobre conjuntos. O programa deverá ler a quantidade de operações, o tipo de operação, e os conjuntos que farão parte das
operações de um arquivo '.txt', cujo formato é explicado abaixo.

## Criação dos dados a serem lidos.

1 - Na primeira linha, escreva um número inteiro, que será referente à quantidade de operações a serem realizadas.<br>
2 - O restante do arquivo consiste em um conjunto padrão de três linhas, sendo elas:<br>
    - A primeira é uma letra, que define uma operação:<br>
        - U para união, <br>
        - I para interseção, <br>
        - D para diferença, <br>
        - C para produto cartesiano.<br>
    - A segunda são os elementos do conjunto 1, separados por vírgula;<br>
    - A terceira são os elementos do conjunto 2, separados por vírgula.<br>
Cada conjunto dessas três linhas será forma uma operação com dois conjuntos, e pode se repetir de forma ilimitada no decorrer do arquivo.<br><br>

Exemplo de arquivo:<br>

4<br>
U<br>
3, 5, 67, 7<br>
1, 2, 3, 4<br>
I<br>
1, 2, 3, 4, 5<br>
4, 5<br>
D<br>
1, A, C, 34<br>
A, C, D, 23<br>
C<br>
3, Banana, 5, 5, A, B, R<br>
1, B, C, D, 1<br>

## Como adicionar o arquivo '.txt' para ser lido

O nome do arquivo '.txt' encontra-se dentro de uma variável, chamada 'nome_arquivo'. Para mudar o arquivo a ser lido, basta trocar
o nome do arquivo dentro desta variável.

Exemplo:
nome_arquivo = 'teste1.txt'

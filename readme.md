## Introdução

Trabalho da disciplina Resolução de Problemas de Natureza Discreta, do segundo período do curso de Ciência da Computação,
sobre conjuntos. O programa deverá ler a quantidade de operações, o tipo de operação, e os conjuntos que farão parte das
operações de um arquivo '.txt', cujo formato é explicado abaixo.

## Criação dos dados a serem lidos.

1 - Na primeira linha, escreva um número inteiro, que será referente à quantidade de operações a serem realizadas.<br>
2 - O restante do arquivo consiste em um conjunto padrão de três linhas, sendo elas:<br>
    2.1 - A primeira é uma letra, que define uma operação:<br>
        2.1.1 - U para união,<br>
        2.1.2 - I para interseção,<br>
        2.1.3 - D para diferença, <br>
        2.1.4 - C para produto cartesiano.<br>
    2.2 - A segunda são os elementos do conjunto 1, separados por vírgula;<br>
    2.3 - A terceira são os elementos do conjunto 2, separados por vírgula.<br>
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

O nome do arquivo texto a ser lido deverá ser passado como parâmetro na linha de comando.
Na linha de comando, digite o comando para executar, adicione um espaço, e o caminho do arquivo texto.<br><br>

Exemplo(linux):<br>
python3 main.py ./teste1.txt

Os nomes dos arquivos texto fornecidos neste trabalho são:<br>
- teste1.txt<br>
- teste2.txt<br>
- teste3.txt<br>
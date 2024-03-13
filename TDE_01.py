'''Alunos: Ana Paula Borowsky de Borba e Anthony Sutil de Oliveira

Operações: 
U = União
I = Interseção
D = Diferença
C = Produto cartesiano

Formato do arquivo .txt

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

'''

numero_operacoes = 4
operacao = "U" 
conjuntoA = [3, 5, 67, 7 ]
conjuntoB = [1, 2, 3, 4]

match (operacao):
    case "U":
        print("União do conjunto A e B")
        resultado = conjuntoA + conjuntoB
        print(set(sorted(resultado)))
    case "I":
        print("Interseção do conjunto A e B")
    case "C":
        print("Produto Cartesiano do conjunto A e B")
    case "D":
        print("Diferença do conjunto A e B")
    case _: 
        print("Opção desconhecida.")


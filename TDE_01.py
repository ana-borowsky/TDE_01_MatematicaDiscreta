'''Alunos: Ana Paula Borowsky de Borba e Anthony Sutil de Oliveira

Operações: 
U = União
I = Interseção
D = Diferença
C = Produto cartesiano
'''

def executaOperacao():
    match (operacao):
        case "U":
            print("União do conjunto A e B")
            resultado = conjuntoA + conjuntoB
            print(set(resultado))
        case "I":
            print("Interseção do conjunto A e B")
            resultado = set(conjuntoA) & set(conjuntoB)
            print(resultado)
        case "C":
            print("Produto Cartesiano do conjunto A e B")
            resultado = [(a, b) for a in conjuntoA for b in conjuntoB]
            print(resultado)
        case "D":
            print("Diferença do conjunto A e B")
            resultado = set(conjuntoA) - set(conjuntoB)
            print(resultado)
        case _: 
            print("Opção desconhecida.")

j = 1
i = 0
conjuntoA = [3, 5, 67, 7]
conjuntoB = [1, 2, 3, 4]

with open('teste1.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    numero_operacoes = int(linhas[0])
    operacao = linhas[j].strip()

while i < numero_operacoes:
    executaOperacao()
    j += 3
    while j < numero_operacoes * 3:
        operacao = linhas[j].strip()
        break
    i += 1

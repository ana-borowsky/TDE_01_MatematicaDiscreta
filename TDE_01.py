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
            print(set(resultado))
        case "D":
            print("Diferença do conjunto A e B")
            resultado = set(conjuntoA) - set(conjuntoB)
            print(resultado)
        case _: 
            print("Opção desconhecida.")

i = 0
j = 1
k = 2
l = 3

with open('teste1.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    numero_operacoes = int(linhas[0])
    operacao = linhas[j].strip()
    conjuntoA = linhas[k].strip().split(',')
    conjuntoB = linhas[l].strip().split(',')

while i < numero_operacoes:
    executaOperacao()
    j += 3
    k += 3
    l += 3
    while j < numero_operacoes * 3:
        operacao = linhas[j].strip()
        conjuntoA = linhas[k].strip().split(',')
        conjuntoB = linhas[l].strip().split(',')
        break
    i += 1

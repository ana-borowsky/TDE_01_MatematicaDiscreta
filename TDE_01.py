#Alunos: Ana Paula Borowsky de Borba e Anthony Sutil de Oliveira

def executaOperacao():
    match (operacao):
        case "U":
            resultado = conjuntoA + conjuntoB
            print(f"União: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case "I":
            resultado = set(conjuntoA) & set(conjuntoB)
            print(f"Interseção: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {resultado}\n")
        case "C":
            resultado = [(a, b) for a in conjuntoA for b in conjuntoB]
            print(f"Produto Cartesiano: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case "D":
            resultado = set(conjuntoA) - set(conjuntoB)
            print(f"Diferença: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case _: 
            print("Opção desconhecida.")

i = 0
j = 1
k = 2
l = 3
nome_arquivo = input("Digite o nome do arquivo .txt (exemplo: teste1.txt): ")
qtd_linhas = 0

with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    numero_operacoes = int(linhas[0])
    operacao = linhas[j].strip().upper()
    conjuntoA = linhas[k].strip().replace(' ', '').split(',')
    conjuntoB = linhas[l].strip().replace(' ', '').split(',')

for m in linhas:
    qtd_linhas += 1

while i < numero_operacoes:
    executaOperacao()
    j += 3
    k += 3
    l += 3

    if j >= qtd_linhas + 1:
        print("Número de operações maior que a quantidade de operações. Por favor redefina a primeira linha do arquivo, ou adicione mais operações.")
        break

    while j < qtd_linhas:
        operacao = linhas[j].strip().upper()
        conjuntoA = linhas[k].strip().replace(' ', '').split(',')
        conjuntoB = linhas[l].strip().replace(' ', '').split(',')
        break
    i += 1

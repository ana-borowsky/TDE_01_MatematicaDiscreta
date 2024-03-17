#Alunos: Ana Paula Borowsky de Borba e Anthony Sutil de Oliveira

def executaOperacao(operacao, conjuntoA, conjuntoB):
    match (operacao):
        case "U":
            resultado = conjuntoA + conjuntoB
            print(f"União: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case "I":
            resultado = set(conjuntoA) & set(conjuntoB)
            print(f"Interseção: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case "C":
            resultado = [(a, b) for a in conjuntoA for b in conjuntoB]
            print(f"Produto Cartesiano: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case "D":
            resultado = set(conjuntoA) - set(conjuntoB)
            print(f"Diferença: conjunto 1 {set(conjuntoA)}, conjunto 2 {set(conjuntoB)}. Resultado: {set(resultado)}\n")
        case _: 
            print("Opção desconhecida.")

nome_arquivo = 'teste1.txt'

with open(nome_arquivo, 'r') as arquivo:
    num_operacoes = int(arquivo.readline())
    for i in range(0, num_operacoes):
        operacao = arquivo.readline().strip().upper()
        conjuntoA = arquivo.readline().strip().replace(' ', '').split(',')
        conjuntoB = arquivo.readline().strip().replace(' ', '').split(',')
        executaOperacao(operacao, conjuntoA, conjuntoB)

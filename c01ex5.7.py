# File: chaos.py
# Chaos program to print side-by-side values
# Programa Caos para imprimir os valores lado a lado
#Para uma versão mais elegante desse exempplo veja o exercício 12 do cap 5.
# by John Zelle, adaptado em: zellepython.wordpress.com

def main():
    print("Este program ilustra uma função caótica")
    x1 = eval(input("Insira a primeira semente entre 0 e 1: "))
    x2 = eval(input("Insira a segunda semente entnre 0 e 1: "))
    print()
    print("Insira     ", x1, " | ", x2)
    print("-------------------------------------------")
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("      ", x1, " | ", x2)

main()

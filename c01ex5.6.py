# File: chaos.py
# Um simples programa que ilustra o comportamento de uma função caótica.
# by John Zelle, adaptado em: zellepython.wordpress.com


def main():
    print("Este Programa ilustra uma função caótica")
    x = eval(input("Insira um número entre 0 e 1: "))
    x2 = x
    x3 = x
    for i in range(100):
        x = 3.9 * x * (1 - x)
        x2 = 3.9 * (x2 - x2*x2)
        x3 = 3.9*x3 - 3.9*x3*x3
        print(x,x2,x3)

main()

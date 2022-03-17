# chaos.py
# Um programa que imprime a quantidade de números definida pelo usuário.
# by John Zelle, adaptado em zellepython.wordpress.com

def main():
    print("Esse programa ilusta uma função caótica")
    x = eval(input("Insira um número entre 0 e 1: "))
    n = eval(input("Quantos números você gostaria de imprimir? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()

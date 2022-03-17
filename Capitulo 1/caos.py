# chaos.py
# Um programa simples para ilustrar uma função caótica.
# by John Zelle, adaptado em zellepython.wordpress.com

def main():
    print("Esse programa ilusta uma função caótica")
    x = eval(input("Insira um número entre 0 e 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

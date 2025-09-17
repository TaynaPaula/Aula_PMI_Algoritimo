a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))

try:
    r = a / b
    print("Resultado: r = %.1f" % r)
except:
    print("Não é possível calcular a divisão")

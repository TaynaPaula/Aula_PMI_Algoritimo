#Ler valores até digitar 0, dizendo se é par ou ímpar
x = 1
while x != 0:
    x = int(input("Digite x: "))
    if x != 0:  # evita dizer que 0 é par
        if x % 2 == 0:
            print("%d é par" % x)
        else:
            print("%d é ímpar" % x)
print("Programa encerrado.")
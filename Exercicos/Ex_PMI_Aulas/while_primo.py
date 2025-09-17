n = int(input("Digite um número inteiro: "))
i = 2

while i < n:
    if n % i == 0:
        print("{} não é primo".format(n))
        break
    i += 1
else:
    print("{} é primo".format(n))

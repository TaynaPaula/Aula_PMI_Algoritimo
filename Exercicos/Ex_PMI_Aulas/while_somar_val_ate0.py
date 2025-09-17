soma = 0
qtde = 0
x = 1

while x != 0:
    x = int(input("Digite x: "))
    if x != 0:
        soma = soma + x
        qtde = qtde + 1

print("Total dos valores digitados = %d" % soma)
print("Quantidade de valores = %d" % qtde)

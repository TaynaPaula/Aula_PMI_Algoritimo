
a = int(input('Informe um número: '))

divisivel2 = (a % 2) == 0  # verifica se o resto da divisão por 2 é zero
divisivel3 = (a % 3) == 0  # verifica se o resto da divisão por 3 é zero

if divisivel2:
    print("é divisível por 2")
else:
    print("não é divisível por 2")

if divisivel3:
    print("é divisível por 3")  
else:
    print("não é divisível por 3")

if divisivel2 and divisivel3:
    print("é divisível por 2 e 3")


#ok
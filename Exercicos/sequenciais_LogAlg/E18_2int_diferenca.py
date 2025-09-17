#Exercicio 18 ----
"""18.	Receba 2 valores inteiros.
 Calcule e mostre o resultado da diferença do maior pelo menor valor."""
a=int(input("Digite o 1º valor inteiro: "))
b=int(input("Digite o 2º valor inteiro: "))
if a>=b:
    dif=a-b
    print(f"O resultado de {a} - {b}, a diferença do maior pelo menor é {dif}.")
else:
    dif=b-a
    print(f"O resultado de {a} - {b}, a diferença do maior pelo menor é {dif}.")





#Exercicio 23 ----
"""23.	Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem.
 Mostre os 4 números em ordem crescente."""
A=int(input("Digite o 1º valor inteiro (ordem crescente): "))
B=int(input("Digite o 2º valor inteiro (ordem crescente): "))   
C=int(input("Digite o 3º valor inteiro (ordem crescente): "))
D=int(input("Digite o 4º valor inteiro: "))         
if D<A:
    print("Ordem crescente D, A, B, C: ", D, A, B, C)
elif D>=A and D<B:
    print("Ordem crescente A, D, B, C: ", A, D, B, C)       
elif D>=B and D<C:
    print("Ordem crescente A, B, D, C: ", A, B, D, C)   
else:
    print("Ordem crescente A, B, C, D: ", A, B, C, D)


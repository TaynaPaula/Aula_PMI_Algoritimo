"""5.	Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). 
Calcule e mostre as raízes reais (considerar que a equação possue2 raízes)."""
#Exercicio 5 -------
a= float(input("Digite o valor de A "))
b= float(input("Digite o valor de b "))
c= float(input("Digite o valor de c "))
D=((b**2)-(4*a*c))
RaizD=D**0.5
R1=(-b+RaizD)/(2*a)
R2=(-b-RaizD)/(2*a) 
print(f"As raízes reais da equação {a}x² + {b}x + {c} = 0 são {R1:.2f} e {R2:.2f}.")

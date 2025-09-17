#Exercicio 20 ----
"""20.	Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula
 AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista,
   calcule e mostre."""
a=int(input("Digite o valor do coeficiente A: "))
b=int(input("Digite o valor do coeficiente B: "))
c=int(input("Digite o valor do coeficiente C: "))
d=(b**2)-(4*a*c)
if d>=0:
    raizd=d**0.5
    r1=(-b+raizd)/(2*a)
    r2=(-b-raizd)/(2*a)
    print(f"As raízes reais da equação {a}x² + {b}x + {c} = 0 são {r1:.2f} e {r2:.2f}.")
else:
    print("Não existem raízes reais para essa equação.")

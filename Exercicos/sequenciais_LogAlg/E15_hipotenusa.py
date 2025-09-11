#Exercicio 15 ----
"""15.	Receba os valores de 2 catetos de um triângulo retângulo.
 Calcule e mostre a hipotenusa"""
a=int(input("Digite o valor do cateto a: "))
b=int(input("Digite o valor do cateto b: "))
hipo=(a**2+b**2)**0.5
print(f"A hipotenusa vai medir {hipo:.2f}")
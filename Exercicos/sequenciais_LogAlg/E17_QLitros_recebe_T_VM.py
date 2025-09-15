#Exercicio 17 ----
"""17.	Calcule a quantidade de litros gastos em uma viagem, 
sabendo que o automóvel faz 12 km/l. 
Receber o tempo de percurso e a velocidade média."""
t=float(input("Digite o tempo de percurso (em horas): "))
v=float(input("Digite a velocidade média (em km/h): "))
Distancia = t * v
Litros = Distancia / 12 
print(f"A quantidade de litros gastos na viagem é {Litros:.2f} litros.")


#ok
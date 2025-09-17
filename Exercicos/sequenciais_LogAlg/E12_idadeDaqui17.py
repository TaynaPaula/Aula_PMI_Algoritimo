#Exercicio 12 ----
"""12.	Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade 
e quantos anos terá daqui a 17 anos."""
nasc=int(input("Em que ano você nasceu? "))
atual=int(input("Em que ano estamos? "))
idade=atual-nasc
apos=idade+17
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
print(f"Em {atual+17} você terá {apos} anos.")



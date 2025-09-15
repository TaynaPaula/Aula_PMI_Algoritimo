#Exercicio 16 ----
"""16.	Receba a quantidade de horas trabalhadas, o valor por hora, 
o percentual de desconto e o número de dependentes. 
Calcule o salário que serão as horas trabalhadas x o valor por hora.
 Calcule o salário líquido (= Salário Bruto – desconto).
A cada dependente será acrescido R$ 100 no Salário Líquido. 
   Exiba o salário a receber"""
H=float(input("Digite a quantidade de horas trabalhadas: "))
ValorH=float(input("Digite o valor por hora trabalhada: ")) 
Desc=float(input("Digite o percentual de desconto (sem o %): "))
Dep=int(input("Digite o número de dependentes: ")) 
SalarioLiquido = ((H*ValorH) - ((H*ValorH)*Desc/100)) + (Dep * 100)
print(f"O salário a receber é R$ {SalarioLiquido:.2f}.")


#ok
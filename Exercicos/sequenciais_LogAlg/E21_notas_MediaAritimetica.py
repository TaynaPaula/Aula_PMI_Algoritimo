#Exercicio 21 ----
"""21.	Receba 4 notas bimestrais de um aluno.
 Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
 a.	Se a média for >= 6,0 exibir “APROVADO”;
b.	Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
c.	Se a média for < 3,0 exibir “RETIDO”."""

B1=float(input("Digite a nota do 1º bimestre: "))
B2=float(input("Digite a nota do 2º bimestre: "))       
B3=float(input("Digite a nota do 3º bimestre: "))
B4=float(input("Digite a nota do 4º bimestre: "))   
Media=(B1+B2+B3+B4)/4
if Media>=6:
    print("APROVADO")       
elif Media>=3 and Media<6:
    print("EXAME")
else:
    print("RETIDO") 
print("Média Aritmética: ", Media)


#ok
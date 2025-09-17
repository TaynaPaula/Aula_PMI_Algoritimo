a= int (input("digite um valor para a:"))
b= int(input("digite um valor para b:"))
try:
    r=a/b;
    print ("Resultado: r= %.lf" %r);
except:
    print("não é possível calcular a divisao")
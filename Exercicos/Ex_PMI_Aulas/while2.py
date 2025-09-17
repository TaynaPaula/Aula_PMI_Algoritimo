soma=0;
qtde=0;
x=1;
while x !=0:
    x=int (input("digite x: "))
    if x != 0:
        soma=soma + x;
        qtde =qtde+1;
    print ("total dos valores digitados = %d" % soma)
    print ("quantidades de valores =  %d" % qtde)
    #Só vai parar no zero
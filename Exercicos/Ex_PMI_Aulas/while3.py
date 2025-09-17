n=int (input("digite um número inteiro"))
i=2;
while i <n:
    r =n %i;
    if r==0:
        print("{} não é primo".format(n))
        break;
    i+=1;
else:
  print(" {} e primo".format (n))
  
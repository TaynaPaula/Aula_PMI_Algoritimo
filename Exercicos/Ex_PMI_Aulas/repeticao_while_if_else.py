n =0;
while n < 100 or n > 500:
    try:
        s = (input("digite um valor no intervalo de [100, 500]:"))
        n = int (s);
    except:
        print("{} não é um número.".format(s));
        n=0;
    else:
        if n <100 or n >500:
            print("o valor lido {} esta forra do intervalo" .format(n));
        else:
            print("o valor lido {} esta ok" .format(n));
    finally:
        print("\n\n");#repetição do código
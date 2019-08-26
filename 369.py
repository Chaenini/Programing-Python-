for total in range(1,99+1) :
    total = str(total)
    n = 0

    if(len(total)==1):
        if int(total[0])%3==0 :
            n+=1

    if(len(total)==2) :
        if int(total[0]) % 3 == 0 :
            n += 1
        if int(total[1]) % 3 == 0 and int(total[1])!=0:
            n += 1

    if(n != 0) :
        print("짝"*n)
    else :
        print(total)
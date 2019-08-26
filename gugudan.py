dan = 2
for a in range(1,9+1) : 
    print(dan,"x",a,"=",dan*a)

print("---------------")

for i in range(2,9+1) :
    for j in range(1,9+1) : 
        if j>7 : 
            break
        if j%2==0 :
            continue
        print(i,"x",j,"=",i*j)

    print("---------------")
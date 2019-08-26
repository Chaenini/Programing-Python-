number = input("숫자를 입력하세요 >>> ")
list = []
sum=0

for x in number : 
    list += x

for i in range(0, len(number)):
    sum += int(list[i])
    
print(sum)
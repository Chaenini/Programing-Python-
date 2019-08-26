#107p
import random
def rolling_dice():
    n = random.randint(1,6) #1<=n<=6인 랜덤수 random(1,6) = 1~5 randint(1,6) = 1~6
    print("6면 주사위를 굴린 결과 : ",n)
#파이썬은 오버로딩이 불가하다 

def rolling_dice(pip):
    n = random.randint(1,pip) #1<=n<=6인 랜덤수 random(1,6) = 1~5 randint(1,6) = 1~6
    print(pip,"면 주사위를 굴린 결과 : ",n)

def rolling_dice(pip, repeat):
    for r in range(1,repeat+1):
        n = random.randint(1,pip) #1<=n<=6인 랜덤수 random(1,6) = 1~5 randint(1,6) = 1~6
        print(pip,"면 주사위를 굴린 결과 : ",r," : ",n)

rolling_dice(6,1)
rolling_dice(6,0)
rolling_dice(6,5)
rolling_dice(6,2)
rolling_dice(6,3)

print()

#109P
def star() : 
    print("*"*5)

star()
star()
star()

#113p
print("♡")
print("♡","♪")
print("♡","♪","♣")
print("♡","♪","♣","♠")
print("♡","♪","♣","♠","★")

#114p
def p (*args) :
    string = ""
    for a in args : 
        string += a
    print(string)

print("♡")
print("♡","♪")
print("♡","♪","♣")
print("♡","♪","♣","♠")

#114p
def p(space, space_num, *args) : 
    string = args[0]
    for i in range(1,len(args)):
        string += (space * space_num)+args[1]
    print(string)

p(",",3,"♡","♪")
p("★",3,"♡","♪","♣")
p("★",3,"♡","♪","♣","♠")

#115p
def star2(ch, *nums):
    #for i in range(1,len(nums)):
        #print (nums[0]* nums[i])
    for n in nums : 
        print(ch * n)

star2("♪",3)
star2("♡",1,2,3)

#116p
def fn(a,b,c,d,e) : 
    print(a,b,c,d,e)

fn(1,2,3,4,5)
fn(10,20,30,40,50)
fn(a=1, b=2, c=3, d=4, e=5)
fn(51, 2, c=3, d=4, e=5)
#fn(d=1, e=2, 3,4,5) = 에러

#118p
def star(mark, repeat, space, space_repeat, line):
    for i in range(line):
        String = ""
        String += (mark*repeat) + (space*space_repeat) + (mark*repeat)
        print(String)

star("※", 3, "_", 2, 3)

#119p
def Hello(msg = "안녕하세요"):
    print(msg + "!")

Hello("하이")
Hello("hi")
Hello()

#120p
def hello2(name, msg="안녕하세요") : 
    print(name+"님, "+msg+" ! ")

hello2("김가영","오랜만 이에요")
hello2("김선옥")
hello2("이채린")

def fn2(a,b=[]):
    b.append(a)
    print(b)

fn2(3)  #[].append(3) = [3]
fn2(5)  #[].append(5) = [5] : x [3,5] : o
fn2(10) #[3,5,10]
fn2(7,[1]) #[3,5,10,7] : x [7,1] : o
#fn2(a=7, b=[1]) : 
    #print([1].append(7))

def gugudan(dan=2):
    for i in range(1,9+1):
        #print(dan,"x",i,"=",dan*i)
        print(str(dan)+"x"+str(i)+"="+str(dan*i))
        print()

gugudan(3)
gugudan(2)
gugudan()

def sum(*numbers):
    sum_value=0
    for number in numbers:
        sum_value +=number
    return sum_value

print("1 + 3 = ",sum(1,3))
print("1 + 3 + 5 + 7 = ",sum(1,3,5,7))


def min(*numbers):
    min_value=0
    for number in numbers : 
        min_value -= number
    return min_value

print("min(3,6,-2) = ", min(3,6,-2))


def max(*numbers):
        max_value=numbers[0]
        for number in numbers : 
                if max_value < number :
                        max_value=number
        return max_value
print("max(4,5,-2,10) = ",max(4,5,-2,10))

def multi_num(multi, start, end) : 
        result = []
        for n in range(start,end):
                if n % multi ==0 : 
                        result.append(n)
        return result

print("multi_num(17,1.200) = ",multi_num(17,1,200))
print("multi_num(3,1,100) = ",multi_num(3,1,100))
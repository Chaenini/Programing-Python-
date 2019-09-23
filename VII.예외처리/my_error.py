#P129

class OddError(Exception):
    def __init__(self,message="홀수 노노"):
        self.message = massage

    def __str__(self):
        return self.message

n=11
try :
    if n % 2 != 0:
        raise OddError  #에러발생
    else :
        print("짝수에요 짝짝 ")   #에러처리

except OddError as e :
    print(e)
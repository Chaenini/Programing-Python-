def min_max(*args):
        min_value = args[0]
        max_value = args[0]
        for a in args:
                if min_value > a :
                        min_value = a
                if max_value < a :
                        max_value = a
        return min_value,max_value

min,max= min_max(52.-3,23,89,-21)
print("최솟값 : ",min,"최댓값 : ",max)
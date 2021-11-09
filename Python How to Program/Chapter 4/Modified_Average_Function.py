def get_average(x,*args):
    if(args == None and x == None):
        print('average() is missing 1 required positional argument.')
        return None
    else:
        return sum(args)+x/len(args)+1

x=1
num1 = get_average(x,2,3,4,5)
print(num1)

num2 = get_average()
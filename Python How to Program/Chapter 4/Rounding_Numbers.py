user_input_one = float(input('Enter a valid amount: '))
user_input_two = int(input('Enter number of digits: '))

def printfloat(input_val, deciplaces):
    print(round(input_val, deciplaces))

printfloat(user_input_one,user_input_two)
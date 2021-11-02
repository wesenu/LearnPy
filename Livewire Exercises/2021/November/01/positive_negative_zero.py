user_input_one = float(input('Enter a valid amount(1): '))
positive_counter = 0
negative_counter = 0
zero_counter = 0
while(user_input_one != -1):
    
    if(0<user_input_one):
        print(f'{user_input_one} is a positive number')
        positive_counter = positive_counter+1

    elif(0>user_input_one and user_input_one!= -1):
        print(f'{user_input_one} is negative number')
        negative_counter = negative_counter +1
    
    elif(user_input_one == 0 ):
        print(f'{user_input_one} is a zero')
        zero_counter = zero_counter +1

    user_input_one = float(input('Enter a valid amount(1): '))

print(f"Positive number: {positive_counter}")
print(f"Negative number: {negative_counter}")
print(f"Zero: {zero_counter}")


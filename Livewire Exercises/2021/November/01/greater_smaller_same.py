#check if two numbers are greater, less or equal

user_input_one = float(input('Enter a valid amount(1): '))
user_input_two =  (input('Enter a valid amount(2): '))

if(user_input_two<user_input_one):
    print(f'{user_input_one} is greater than {user_input_two}')

elif(user_input_two>user_input_one):
    print(f'{user_input_one} is less than {user_input_two}')

else:
    print(f'{user_input_one} is equal to {user_input_two}')

    
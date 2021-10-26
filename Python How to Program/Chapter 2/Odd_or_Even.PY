#Use if statements to determine whether an integer is odd or even.

user_input = int(input('Enter value: '))
if(user_input % 2 == 0):
    print(f'Value {user_input} is Even')
else:
    print(f'Value {user_input} is Odd')
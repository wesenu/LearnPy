#Write a script that inputs a nonnegative integer and 
# displays whether it is a perfect number or not.


user_input_perfect_number = int(input('Enter your integer value: '))
num_sum = 0
for i in range(1, int(user_input_perfect_number)):
    if(user_input_perfect_number%i==0):
        num_sum = num_sum + i
    
if(num_sum == user_input_perfect_number):
    print(f'{user_input_perfect_number} is a perfect number')
else:
    print(f'{user_input_perfect_number} is NOT a perfect number')
    
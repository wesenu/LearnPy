# Develop a sentinel-controlled-repetition script 
# that prompts the user to input the number of does living in the farm and 
# the number of rabbits born in a specific month. 
# Then, calculate and display the combined average number of rabbits born per doe.




user_input_num_of_does = int(input('Enter the number of does in the rabbit colony (-1 to end): '))
total_does = 0
total_babies = 0

while(user_input_num_of_does !=-1):

    user_input_babies_born = int(input('Number of baby rabbits born in the past month: '))

    total_does = total_does + user_input_num_of_does
    total_babies = total_babies + user_input_babies_born

    print(f'On average {float(user_input_babies_born/user_input_num_of_does):.2f} baby rabbits were born for each doe')

    user_input_num_of_does = int(input('Enter the number of does in the rabbit colony (-1 to end): '))

print(f'Total number of baby rabbits for each doe so far: {float(total_babies/total_does):.2f}')


    

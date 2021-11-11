# Lets the user play a multiplication game. 
# Randomly selects two numbers between 1 and 10. 
# Asks the player for the product of both numbers. 
# If the player answers correctly, 
# they are asked if they want to play again

import random

def generate_random_number():
    val_one = random.randrange(1,11)
    val_two = random.randrange(1,11)
    return val_one, val_two

def product(val_one, val_two):
    return val_one*val_two

def print_val(value):
    print(f'Value: {value}')


def play_game():
    val_one, val_two = generate_random_number()
    product_val = product(val_one, val_two)
    print_val(val_one)
    print_val(val_two)
    user_input = int(input('Enter the product: '))
    if(user_input == product_val):
        print("Correct answer.")
        play_again = input('Do you want to play again? [Y/y]or[N/n]: ')
        if(play_again == 'Y' or play_again == 'y'):
            return False
        else:
            return True
        
    else:
        print("Wrong answer.")
        return True


is_game_over = False
correct_answer_counter = 0
while(is_game_over != True):
    is_game_over = play_game()
    if(is_game_over == False):
        correct_answer_counter +=1

print(f'Number of correct answers: {correct_answer_counter}')
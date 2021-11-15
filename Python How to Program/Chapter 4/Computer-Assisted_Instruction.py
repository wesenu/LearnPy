import random

def correct_answer_encourage():
    random_number = random.randrange(1,4)
    if(random_number == 1):
        print('Very Good')
    elif(random_number == 2):
        print('Nice Work')
    elif(random_number == 3):
        print('Keep up the good work!')

def wrong_answer_encourage():
    random_number = random.randrange(1,4)
    if(random_number == 1):
        print('No. Please try again')
    elif(random_number == 2):
        print('Wrong. Try once more')
    elif(random_number == 3):
        print('No. Keep trying')

def get_difficulty():
    print('Enter your difficulty (1 Easy/2 Hard): ', end=" ")
    return get_user_input()

def get_type():
    print('1: Addition')
    print('2: Subtraction')
    print('3: Multiplication')
    print('4: Division')
    print('5: Mixture')
    print("Enter Type for your problem: ", end=" ")
    return get_user_input()

def generate_two_numbers(difficulty):
    if(difficulty == 1):
        num_one = random.randrange(1,10)
        num_two = random.randrange(1,10)
        
    elif(difficulty == 2):
        num_one = random.randrange(1,100)
        num_two = random.randrange(1,100)
        
    return (num_one, num_two)
    
def win_condition_mul(user_input, num_one, num_two):
    if(user_input == (num_one*num_two)):
        return True
    else:
        return False

def win_condition_add(user_input, num_one, num_two):
    if(user_input == (num_one+num_two)):
        return True
    else:
        return False
        
def win_condition_sub(user_input, num_one, num_two):
    if(user_input == (num_one-num_two)):
        return True
    else:
        return False
    
def win_condition_div(user_input, num_one, num_two):
    if(user_input == (num_one//num_two)):
        return True
    else:
        return False

def game_won_try_again():
    correct_answer_encourage()
    print('Do you want to try again?: Y/y or N/n', end=" ")
    play_again = input()
    if(play_again == 'Y' or play_again == 'y'):
        return True
    else:
        return False

def game_wrong_answer():
    wrong_answer_encourage()
    print('Enter value again: ',end=" ")
    return get_user_input()

def get_user_input():
    user_input = int(input())
    return user_input

def checker(num_one, num_two, problem_type):
    if(problem_type == 1):
        is_won = win_condition_add(get_user_input(), num_one, num_two)
    elif(problem_type == 2):
        is_won = win_condition_sub(get_user_input(), num_one, num_two)
    elif(problem_type == 3):
        is_won = win_condition_mul(get_user_input(), num_one, num_two)
    elif(problem_type == 4):
        is_won = win_condition_div(get_user_input(), num_one, num_two)
        
            
    if(is_won == False):
        while(is_won != True):
            if(problem_type == 1):
                is_won = win_condition_add(game_wrong_answer(), num_one, num_two)
            elif(problem_type == 2):
                is_won = win_condition_sub(game_wrong_answer(), num_one, num_two)
            elif(problem_type == 3):
                is_won = win_condition_mul(game_wrong_answer(), num_one, num_two)
            elif(problem_type == 4):
                is_won = win_condition_div(game_wrong_answer(), num_one, num_two)
            
            if(is_won):
                break
    
def start_game():
    problem_type = get_type()
    difficulty = get_difficulty()
    num_one, num_two = generate_two_numbers(difficulty)
    is_won = False
    
    if(problem_type == 1):
        print(f'What is the Addition of {num_one} and {num_two}: ',end=" ")
        checker(num_one,num_two,problem_type)
        return game_won_try_again()

    elif(problem_type == 2):
        print(f'What is the Subtraction of {num_one} and {num_two}: ',end=" ")
        checker(num_one,num_two,problem_type)
        return game_won_try_again()
    
    elif(problem_type == 3):
        print(f'What is the Multiplication of {num_one} and {num_two}: ',end=" ")
        checker(num_one,num_two,problem_type)
        return game_won_try_again() 
    
    
    elif(problem_type == 4):
        print(f'What is the Division of {num_one} and {num_two}: ',end=" ")
        checker(num_one,num_two,problem_type)
        return game_won_try_again()
    
    if(is_won == True):
        return game_won_try_again()
        

    
               
main = start_game()
while(True):
    if(main == False):
        break
    else:
        main = start_game()
                
            

            
        

        
            
            


    


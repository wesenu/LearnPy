import random

def tortise_move():
    rand_move = random.randrange(1,11)
    if(rand_move<=5 and rand_move>=1):
        move_to_add = 3
    
    elif(rand_move>=6 and rand_move<=7):
        move_to_add = -6
    
    elif(rand_move>=8 and rand_move<=10):
        move_to_add = 1

    return move_to_add

def hare_move():
    rand_move = random.randrange(1,11)
    if(rand_move>=1 and rand_move<=2):
        move_to_add = 0
    
    elif(rand_move>=3 and rand_move<=4):
        move_to_add = 9

    elif(rand_move == 5):
        move_to_add = -12

    elif(rand_move>=6 and rand_move<=8):
        move_to_add = 1

    elif(rand_move>=9 and rand_move<=10):
        move_to_add = -2

    return move_to_add

def win_condition(hare_position,tortise_position):
    if(hare_position>=70):
            print("Hare Won, Yuch")
            return True
    elif(tortise_position>= 70):
            print("Yay Tortise won")
            return True
    elif(hare_position == tortise_position and (tortise_position>=70 and hare_position>=70)):
            print('It is a fucking tie, underdog tortise')
            return True

def play_game():

    tortise_position = 1
    hare_position = 1
    print("Race starts!")
    print(f'Hare at position: {hare_position}')
    print(f'Tortise at position: {tortise_position}')

    while(True):
        tortise_position += tortise_move()
        hare_position += hare_move()
        
        if(tortise_position<1):
            print('Tortise fell, Back To start')
            tortise_position = 1
        
        if(hare_position < 1):
            print('Hare fell, Back To start')
            hare_position = 1
        
        
        print(f'H: {hare_position}', end='\t')
        print(f'T: {tortise_position}', end='\t')
        print()
        
        if(tortise_position == hare_position):
            print(f'Tortise bit hare at {hare_position} OUCH!!!!!')
        
        if(win_condition(hare_position, tortise_position)):
            break

play_game()        

        
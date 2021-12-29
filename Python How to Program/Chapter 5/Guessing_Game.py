import random

actors_name = ['Sean Bean', 'Mark Addy', 'Nikolaj Coster-Waldau', 'Michelle Fairley', 'Lena Headey']

characters_name = ['Ned Stark', 'Robert Baratheon', 'Jaime Lannister', 'Catelyn Stark', 'Cersei Lannister']

character_actor = list(tuple(zip(characters_name, actors_name)))

guess_counter, correct_counter = 0,0


while (correct_counter<5):
    
    print(f'Correct Answers: {correct_counter}')
    print(f'Number of Tries: {guess_counter}')

    char_index = random.randrange(0,len(character_actor))
    current_character = characters_name[char_index]
    
    print(f'\n\n{current_character}')
    actor_name_input = input("Enter the name of the actor: ")

    my_input = (current_character, actor_name_input)
    
    if (my_input in character_actor):
        correct_counter += 1
        character_actor.remove(my_input)
        characters_name.remove(current_character)       

    else:
        print('wrong answer')
    guess_counter +=1
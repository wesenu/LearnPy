import random

def type_one(char_list, num_list):
    generate_id = ''
    generate_id += random.choice(char_list)
    generate_id += str(random.choice(num_list)) 
    generate_id += str(random.choice(num_list))
    return generate_id

def type_two(char_list, num_list):
    generate_id = ''
    generate_id += str(random.choice(num_list)) 
    generate_id += random.choice(char_list)
    generate_id += str(random.choice(num_list))
    return generate_id

def type_three(char_list, num_list):
    generate_id = ''
    generate_id += str(random.choice(num_list)) 
    generate_id += str(random.choice(num_list))
    generate_id += random.choice(char_list)
    return generate_id

import random
import numpy
import generate_id

char_list = [chr(i) for i in range(ord('a'), ord('g'))]
num_list = list(range(0,5))

id_list = []

for _ in range(8000):
    choice = random.choice(range(1,4))
    
    if choice == 1:
        user_id = generate_id.type_one(char_list, num_list)
    elif choice == 2:
        user_id = generate_id.type_two(char_list, num_list)
    elif choice == 3:
        user_id = generate_id.type_three(char_list, num_list)
        
    id_list.append(user_id)

id_list = numpy.unique(id_list)
print(id_list)
print(len(id_list))
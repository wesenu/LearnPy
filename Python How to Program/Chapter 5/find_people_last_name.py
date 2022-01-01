import random
list_name_tuples = []
first_name = ['Michael','Christopher','Jessica',
              'Matthew','Ashley','Jennifer','Joshua',
              'Amanda','Daniel','David','James',
              'Robert','John','Joseph','Andrew',
              'Ryan','Brandon','Jason','Justin',
              'Sarah','William','Jonathan','Stephanie',
              'Brian','Nicole']

last_name = ['Jones', 'Kim', 'De la curze', 'Kutcher']

for _ in range(len(first_name)):
    person_name = (random.choice(first_name), random.choice(last_name))
    list_name_tuples.append(person_name)
    

jones_filter = list(filter(lambda x: x[1]== 'Jones', list_name_tuples))
print(jones_filter)
#print(list_name_tuples)
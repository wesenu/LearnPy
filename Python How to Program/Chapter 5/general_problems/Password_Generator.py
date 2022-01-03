from itertools import permutations
def convert_to_list(mylist):
    my_new_list = []   
    for i in range(len(mylist)):
        my_string = ''
        for j in range(len(mylist[i])):
            my_string +=mylist[i][j]
            j+=1
        my_new_list.append(my_string)
        i+=1
        
    return my_new_list
    

user_input = input('Enter a string consisting of 2 letters and 1 number: ')
password_list = convert_to_list(list(permutations(user_input)))
print(password_list)

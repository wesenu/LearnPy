# Create a function cube_list that cubes each element of a list. 
# Call the function with the list numbers containing 1 through 10

def cube_list(mylist):
    for i in range(len(mylist)):
        mylist[i] = mylist[i]**3
        
def cube_list_test():        
    example_list = []
    for i in range(1,10):
        example_list.append(i)
    
    print(example_list)
    cube_list(example_list)
    print(example_list)


# empty list named characters and a += augmented assignment  
# to convert the string 'Birthday' into a list of its characters

def convert_char_to_list():
    char_list = []
    char_list+=('Birthday') 
    print(char_list)






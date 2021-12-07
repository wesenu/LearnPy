# Create a function cube_list that cubes each element of a list. 
# Call the function with the list numbers containing 1 through 10


def cube_list_test():
    mylist = []
    for i in range(10):
        mylist.append(i)
    return mylist

mylist = cube_list_test()
print(mylist)

def cube_list(list):
    for i in range(len(list)):
        list[i] = list[i]**3

cube_list(mylist)
print(mylist)



# empty list named characters and a += augmented assignment  
# to convert the string 'Birthday' into a list of its characters

def convertchar():
    characters = []

    characters += 'Birthday'
    print(characters)

convertchar()

#Create a single element tuple
def single_element():
    singleTuple = (123.45, )
    print(singleTuple)
single_element()

#Create high low tuple with day string and 2 temp ints -> then have access to it and unpack it

today_weather = ('Monday', 91, 21)
print(today_weather)
temp = []
day, temp = today_weather
print(day) 
print(temp)


# Create a function cube_list that cubes each element of a list. 
# Call the function with the list numbers containing 1 through 10
def cube_list_test():
    mylist = []
    for i in range(10):
        mylist.append(i)
    return mylist


def cube_list(list):
    for i in range(len(list)):
        list[i] = list[i]**3



# empty list named characters and a += augmented assignment  
# to convert the string 'Birthday' into a list of its characters
def convertchar():
    characters = []

    characters += 'Birthday'
    print(characters)


#Create a single element tuple
def single_element():
    singleTuple = (123.45, )
    print(singleTuple)


#Create high low tuple with day string and 2 temp ints -> then have access to it and unpack it
def wether_reporta():
    today_weather = ('Monday', (91, 21))
    print(today_weather)
    temp = []
    day, temp = today_weather
    print(day)
    print(temp)
    # Error in unpacking 


#create 3 name list, use for loop and enum to iterate
def names_enum():
    name = ['Abu', 'Haz', 'Sera']
    for i, j in enumerate(name):
        print(f'{i} : {j}')




#create lsit from 1 to 15 and perform operations
def slicing_check():
    values = list(range(1,16))
    print(values)
    
    #select even numbers
    for i, j in enumerate(values):
        if(j%2 == 0):
            print(f'index:{i}  value: {j}')
            
    #replace index 5 to 9 with zero val and print
    for i in range(5, 10):
        values[i] = 0
    print(values)
    
    #keep only first 5 element and print
    values[5:] = []
    print(values)   
    
    #delete all of the element by slice
    values[:] = []
    print(values)


    
#create list from 1 to 15 and using del functions
def del_functions():
    mylist = list(range(1,16))
    print(mylist)
    
    #delete first four elements
    del mylist[:4]
    print(mylist)
    
    #delete every other algo
    del mylist[::2]
    print(mylist)
 
    
#create food list and use sort
def sort_func():
    food = ['Cookies', 'pizza', 'Grapes','apples', 'steak','Bacon']
    print(food)
    food.sort()
    print(food)
    
# five num list use list index to search 43 and 44 (44 error) no value error should happen
def list_index():
    mylist = [67,12,46,43,13]
    key1 = 43
    key2 = 44
    key_found(mylist, key1)
    key_found(mylist, key2)
    
def key_found(mylist, mykey):
    if mykey in mylist:
        print(f'Found Key:{mykey} in index:{mylist.index(mykey)}')
    else:
        print(f'Key:{mykey} not found')
        

#create a color list and perform operations
def list_operations():
    rainbow = ['green', 'orange', 'violet']
    
    #Get violet index and add red to that place
    myindex = rainbow.index('violet')
    print(rainbow)
    print(myindex)
    rainbow.insert(myindex, 'red')
    print(rainbow)
    
    #append 'yellow'
    rainbow.append('yellow')
    print(rainbow)
    
    #reverse elements
    rainbow.reverse()
    print(rainbow)
    
    #remove orange
    rainbow.remove('orange')
    print(rainbow)
    
        
#create tuples and cube in list using list compreshion
def list_compre():
    mylist = [(x, x**3) for x in range(1,6)]
    print(mylist)

#create list compre to create list of multiples of 3 less than 30
def multi_list():
    mylist = [x for x in range(3,30,3)]
    print(mylist)    
    

#a generator expression that cubes the even integers in a list
# containing 10, 3, 7, 1, 9, 4 and 2. list to create a list of the results
def generat_exp():
    mylist = [10, 3, 7, 1, 9, 4, 2]
    
    newlist = list(value**3 for value in mylist if value%2 == 0)
    
    newlist = list(filter(isEven, mylist))
    for i , j in enumerate(newlist):
        newlist[i] = j**3
    
    newlist = list(filter(lambda x: x%2 !=0, mylist))
    print(newlist)
    
    mailist = list(map(lambda x: x**2, mylist))
    print(mailist)
    
def isEven(x):
    return x%2==0



#create func from 1 to 15 to do the following
def lamdafunc():
    mylist = [values for values in range(1,16)]
    print(mylist)
    
    #filer with lamda for even elements and make list
    mylistv1 = list(filter(lambda x: x%2==0, mylist))
    print(mylistv1)
    
    #use map with lamda to square elements
    mylistv1 = list(map(lambda x: x**2, mylist))
    print(mylistv1)
    
    #filer even and the map and square with list
    mylistv1 = list(map(lambda x: x**2, filter(lambda x: x%2==0, mylist)))
    print(mylistv1)
    
    
#create func for list of tuples to change set of farenheigh to celiceus
def convertemp():
    faren = [41, 32, 212]
    mylist = list(map(lambda x: (x,(x-32)*(5/9)), faren))
    print(mylist)
    

#food list find small string iwth min and use key func
def fooditem():
    foods = ['Cookies', 'pizza', 'Grapes','apples', 'steak', 'Bacon']
    print(min(foods))
    print(min(foods, key=lambda s:s.lower()))
    
#use 2 int list to sum a new list using zip
def myzip():
    mylist = list(range(1,16))
    mylistv1 = list(range(1,16))
    mylistv2 = list((a + b) for a, b in zip(mylist, mylistv1))
    
    print(mylist)
    print(mylistv1)
    print(mylistv2)
    

# 2x3 list do the follwoing
def two_dimen():
    t = [[10,7,3], [20,4,17]]
    average = 0
    total = 0
    # get average using for statements
    for i in t:
        for j in i:
            average += j
            total +=1
    print(total)
    print(average)
    print(average//total)
    
two_dimen()
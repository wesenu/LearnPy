# This is to ask the user to enter 10 values and print them

amount_of_values = 10
#for i in range(0, amount_of_values+1):
#   user_input = int(input('Enter an integer value: '))
#    print(user_input)

myList=[]
for i in range (0, amount_of_values):
    user_input = int(input('Enter an integer value: '))
    myList.append(user_input)

for i  in range(len(myList)):
    print(myList[i])

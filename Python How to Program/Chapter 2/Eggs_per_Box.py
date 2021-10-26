#Typically 6 eggs fit in one box. 
# Write a script to calculate the number of boxes a farmer needs to store 28 eggs.
#The script will also determine how many eggs are placed in the last uncompleted box, 
# and how many additional eggs are needed to fill this last box.


eggs_per_box = 6

print(f'This is a program to determine boxes per {eggs_per_box} eggs')

number_of_eggs = int(input('Enter the amount of eggs you have: '))
final_basket_eggs = number_of_eggs % eggs_per_box

if(final_basket_eggs>0):
    print(f'You have put {final_basket_eggs} eggs in your final basket')
    print(f'You have {eggs_per_box - final_basket_eggs} spaces left in the final basket of eggs')
    print(f'You need {round(number_of_eggs / eggs_per_box)} baskets to fill up {number_of_eggs} eggs')
else:
    print(f'You need {round(number_of_eggs / eggs_per_box)} baskets to fill up {number_of_eggs}')

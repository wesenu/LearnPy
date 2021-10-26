#Jonah wants to distribute 22 marbles among his
#4 friends. All friends should receive an equal amount of marbles. 
# Write a script that can determine if this is possible


amount_Of_Marbles = int(input('Enter the amount of marbles: '))
amount_Of_Friends = 4

equal_Marbles= int(amount_Of_Marbles/amount_Of_Friends)

print(f'Distributed {equal_Marbles} marbels equally among {amount_Of_Friends} number of friends with  remainder of {amount_Of_Marbles % amount_Of_Friends}')
# Write a script that inputs a number of seconds from the user.
# Calculate the number of hours, minutes, and remaining seconds. 
# Print them separated by “ - ”.


user_input = int(input('Enter number of seconds: '))

time_hours = int(user_input//3600)
user_input = user_input % 3600

time_min = int(user_input//60)
user_input = user_input % 60

print(f'{time_hours} - {time_min} - {user_input}')
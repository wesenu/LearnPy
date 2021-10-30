# Reimplement your script to use a loop that in an iterative process “picks off” the 
# hours, minutes, and remaining seconds using the // and % operators




# TODO: Implement this later. Do not understand the need to re-write the entire thing.

user_input = int(input('Enter number of seconds: '))
time_hours = 0
time_min = 0
while(user_input != 0):
    time_min = int(user_input//60)
    user_input = user_input % 60

print(f'{time_hours} - {time_min} - {user_input}')
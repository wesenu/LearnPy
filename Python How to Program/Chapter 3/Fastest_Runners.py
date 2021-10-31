# Use a loop to find the fastest and second fastest from 10 runners whose speeds are entered.

from typing import _SpecialForm


fastest = 0
fastest_two = 0
for i in range(10):
    user_input = int(input(f'Enter speed for runner {i+1}: '))
    if(fastest<user_input):
        fastest = user_input
    else:
        if(fastest_two<user_input and user_input<fastest):
            fastest_two = user_input


print(f'Fastest runner was {fastest} m/sec')
print(f'Second fastest runner was {fastest_two} m/sec')
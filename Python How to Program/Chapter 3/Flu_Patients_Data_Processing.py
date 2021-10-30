# Write a script in which the user can input the number of reported infections per day over one week. 
# Calculate the total, average, smallest, and largest of these values. 
# Write your script using a loop structure.

total_infected = 0
high_infected = 0
i = 0
while(i < 7):
    infection_input= int(input(f'Enter the amount of infected on day {i+1}: '))
    if(infection_input<0):
        print(f'Please be serious, enter valid numbers')
    else:
        total_infected = total_infected + infection_input
        if(min_infected>infection_input):
            min_infected = infection_input
        if(high_infected<infection_input):
            high_infected = infection_input
        i = i + 1

print(f'Total infected: {total_infected}')
print(f'Highest infection per day: {high_infected}')
print(f'Lowest infection per day: {min_infected}')
print(f'Average infection per week: {round(float(total_infected/7))}')

# While exercising, you can use a heart-rate monitor 
# to see that your heart rate stays within a safe range. 
# formula for calculating your maximum heart rate in beats per minute is 
# 220 minus your age in years.
# Your target heart rate is 50–85% of your maximum heart rate.
# Ask users their age and print the details

user_input = int(input('Enter your age: '))

user_max_heart_rate = 220 - user_input

min_heart_range = user_max_heart_rate - (user_max_heart_rate * 0.5)
max_heart_range = user_max_heart_rate - (user_max_heart_rate * 0.15)

print(f'Your age is {user_input}, your max heart rate is {user_max_heart_rate}')
print(f'Your minimum range of heartbeat should be at {round(min_heart_range)}')
print(f'While your maximum range of heart beat should be near {round(max_heart_range)}')
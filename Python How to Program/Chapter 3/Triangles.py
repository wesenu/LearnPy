# Write a script where a user can input the length of the three sides of a triangle. 
# The script should determine if it is an equilateral triangle or not.

user_input_triangle_first = int(input('Enter lengeth of side 1: '))
user_input_triangle_second = int(input('Enter lengeth of side 2: '))
user_input_triangle_third = int(input('Enter lengeth of side 3: '))

if(user_input_triangle_first == user_input_triangle_second and user_input_triangle_first == user_input_triangle_third):
    print(f"This trangle is an equilateral triangle where everyside is {user_input_triangle_first}")
else:
    print(f"This trangle is not an equilateral triangle")
    print(f'Side one is: {user_input_triangle_first}')
    print(f'Side two is: {user_input_triangle_second}')
    print(f'Side three is: {user_input_triangle_third}')

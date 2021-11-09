# Implement a radians function that 
# returns the radian equivalent of a degree.
# Use this function to print a chart all degrees 
# ranging from 1° to 180°
import math

def rad_to_degree(user_input):
    """[summary]
    Takes degree as input and returns a radian equivalent of a degree
    Args:
        user_input ([int]): [current value of the iterative degree]

    Returns:
        rad [float]: [returns radian equivalent of a degree]
    """
    rad = user_input * math.pi / 180
    return rad


input_val = int(input('Enter values in degree: '))
print(f'Degree\t Randian Point')


if(input_val>180 and input_val<0):
    print(f'This is not allowed your dork. Go check you values again')

else:
    for i  in range(input_val):
        rad = rad_to_degree(i)
        print(f'{i}\t {round(rad,2)}')


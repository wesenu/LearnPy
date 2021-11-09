import random

def get_random_point(*args):
    random_point_one = random.randrange(1,100)
    random_point_two = random.randrange(1,100)
    return (random_point_one, random_point_two)


def calc_slope(point_x1, point_x2, point_y1, point_y2):
    delta_x = point_x2 - point_x1
    delta_y = point_y2 - point_y1
    slope = delta_y/delta_x
    return slope

varible_x1, varible_y1= get_random_point()
varible_x2, varible_y2= get_random_point()

slope = calc_slope(varible_x1, varible_x2, varible_y1,varible_y2)
print (slope)
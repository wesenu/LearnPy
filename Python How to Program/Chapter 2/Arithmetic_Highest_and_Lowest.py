# Write a script that inputs the grades (in integers)of 3 courses from the user. 
# First display the average grade of the three courses, 
# and then the names 
# and the grades of the courses with the highest and the lowest grades.


course_one = int(input('Enter grade one: '))
course_two = int(input('Enter grade two: '))
course_three = int(input('Enter grade three: '))

print(f'The average of the three courses is: {float((course_one+course_two+course_three)/3)}')

print(f'The highest course was {max(course_three,course_one,course_two)}')
print(f'lowest grade course was {min(course_two, course_one, course_three)}')

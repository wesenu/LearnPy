c = [-45, 6, 0, 72, 1543]
print(c)
print(f'length of c = {len(c)}')
c[0] = 1
print(f'This is C after changing index 0')
print(c)

print()
print()

a_list = []
print(a_list, end=' ')
print('= a_list is empty')
for i in range (1,6):
    a_list += [i]
print('This is after appending a_list')    
print(a_list)


print()
print()

list1 = [10,20,30]
list2 = [40, 50]
list3 = list1 + list2
print(f'This is list 1 {list1}')
print(f'This is list 2 {list2}')
print(f'This is list 3 after concatenating {list3}')

print()
print()


numbers = [1,2,3,4,5]
print(numbers)
numbers +=(6,7)
print(numbers)

number1 = 90
number2 = 30
print("num1:", number1)
print("num2:",number2)
number1, number2 = (number2, number1)
print(f'{number2} that num2 and {number1} is num1')

print()
print()

colors = ['red', 'blue', 'yellow']
print(list(enumerate(colors)))
for index, value in enumerate(colors):
    print(f"{index},{value}")
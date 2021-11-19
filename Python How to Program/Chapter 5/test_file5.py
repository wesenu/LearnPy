c = [45, 6, 0, 7, 1543]
print(c)
print('length of array is = ', len(c))
a = 0
b = 1
c[1] = 3
print(c[a+b])
print(c)

print(c[0]+c[1]+c[2])
a_list = []
for i in range(1, 6):
    a_list.append(i)
    
print(a_list[0])

list1 = [10, 20, 30]
list2 = [40, 50]
conlist = list1+list2
print(conlist)
conlist[0:3] = ['HANA', 'DUL', 'SET'] 
print(conlist)
conlist[0:3] = []
print(conlist)

student_tuple = ()
print(len(student_tuple))
student_tuple += (10,20,30,40,50)
print(len(student_tuple))
print(student_tuple)
AB = list(enumerate(student_tuple))
print(AB)

for index, value in enumerate(student_tuple):
    print(f'{index}: {value}')
  
#high_low = (input('Enter day: '), int(input('Enter Highest Temp: ')), int(input('Enter Lowest Temp: ')))
#for index, value in enumerate(high_low):
   # print(f'{index} and {value}')
   
test_list = list(i for i in range(1,16))
print(test_list)
print(test_list[1:len(test_list):2])
test_list[5:10] = [0] * len(test_list[5:10])
print(test_list)
test_list[5:len(test_list)] = []
print(test_list)
test_list[:] = []
print(test_list)

for index, value in enumerate(test_list):
    print(f'{index}: {value}')
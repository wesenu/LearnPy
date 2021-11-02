#testing if (int >2) is prime or not. If not, get smallest divisor

x = int (input("Enter integers greater than 2: "))
smallest_Divisor = None

for i in range (2, x):
    if (x%i == 0):
        smallest_Divisor = i
        break
if(smallest_Divisor!= None):
    print(f'The smallest divisor is for {x} is {smallest_Divisor}')
else:
    print(f'{x} is a prime number')
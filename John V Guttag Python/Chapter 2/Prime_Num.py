print("This is to sum up the prime numbers between 1 to 1000")

last_number = 1000
sum_of_prime = 2

for i in range(2, last_number+1):
    j = 2
    for j in range(2, i):
        if(int(j%i) == 0):
            j = i
            break;
    if(int(j % i) == 1):
        sum_of_prime = sum_of_prime + 1
    



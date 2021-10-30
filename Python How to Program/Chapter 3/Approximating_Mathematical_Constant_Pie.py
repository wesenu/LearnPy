# Write a script that computes the value of π from the following infinite series. 
# Print a table that shows the value of π approximated by one term of this series

denominator = 1
sum_value = 0
print('Term\tValue')
for i in range(100):
    if(i%2==0):
        sum_value = sum_value + 4/denominator
    else:
        sum_value = sum_value - 4/denominator
    print(f'{i:>2}\t{sum_value:.5f}')
    denominator = denominator +2
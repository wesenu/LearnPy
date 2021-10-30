import datetime

def recur_fibo(n):
    if (n<=1):
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))



user_input_term_position = int(input('Enter the term for the series: '))
print('Fibonacci Series: ')
print('Term\t Value')

for i in range(user_input_term_position):
    print(f'{i:>2} \t {recur_fibo(i):>5}')

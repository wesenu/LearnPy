# Starting with 200 bacteria, the growth in the
# number of bacteria after n hours is calculated as follows: B = 200 × 2^n. 
# Print the numberof bacteria after 0, 5, 10, and 15 hours in table format


print("This is to show the bacteria.")

print("Hour\t Number of Bacteria")
for n in range(0,16,5):
    print(f'{n}\t {200 * 2**n}')

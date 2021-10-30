# Reimplement Table with Number of Bacteria from 
# Chapter 2 and aligned the corners



print("This is to show the bacteria.")

print("Hour\t Number of Bacteria")
for n in range(0,16,5):
    print(f'{n:>3}\t {(200 * 2**n):>18}')
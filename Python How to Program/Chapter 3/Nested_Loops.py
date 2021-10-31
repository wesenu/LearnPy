# Write a script that displays the following triangle patterns separately, one below the other.


def Pattern_One():
    row_max = 10
    for i in range(0, row_max+1):
        for j in range(i):
            print('*', end=" ")
        print()

def Pattern_Two():
    row_max = 10
    for i in range(row_max,0,-1):
        for j in range(i):
            print('*', end=" ")
        print()

def Pattern_Four():
    row_max = 10
    asterisk = 1
    for i in range(row_max,0, -1):
        for k in range(i):
            print(" ", end=" ")
        for j in range(asterisk):
            print('*', end=" ")
        asterisk = asterisk + 1
        print()

def Pattern_Three():
    row_max=10
    asterisk = 10
    for i in range(0, row_max):
        for k in range(i):
            print(" ", end=" ")
        for j in range(asterisk):
            print('*', end=" ")
        asterisk = asterisk - 1
        print()

Pattern_One()
print()
Pattern_Two()
print()
Pattern_Four()
print()
Pattern_Three()
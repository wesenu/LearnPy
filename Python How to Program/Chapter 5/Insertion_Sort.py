import random

def sort_list(mylist):
    for i in range(1, len(mylist)):
        key = mylist[i]
        j = i-1
        while j>=0 and mylist[j] > key:
            mylist[j+1] = mylist[j]
            j = j-1
        mylist[j+1] = key
    return mylist
    




mylist = []

for _ in range(10):
    n = random.randint(0,100)
    mylist.append(n)

print(mylist)
newlist = sort_list(mylist)
print(newlist)


    
import numpy as np


mylist = ['a','b','c','d','e','b','c','a']

def clean_list(list_mine):
    return list(np.unique(list_mine))
            
my_new_list = clean_list(mylist)
print(mylist)
print(my_new_list)

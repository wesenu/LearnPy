# Write a function that accepts a string as input
# isolates the different unique letters


# ignore ignoring punctuation, spaces, and case sensitivity
# use lower() for case sensitive string

import string

def GetKey(myInput):
    return myInput.translate(None, string.punctuation)



user_input = input('Enter your string: ')

new_user_input = GetKey(user_input)
print(new_user_input)

def is_palindrome(mystring):
    mylist = []
    mylist += mystring
    mystring2= ''
    for _ in range(len(mylist)):
        myelement = mylist.pop()
        mystring2 +=myelement

    del mylist
    return (mystring2 == mystring)    



mystring1 = input('Enter a string: ')
if(is_palindrome(mystring1.lower())):
    print(f'The string {mystring1} is a palindrome')
else:
    print(f'The string {mystring1} is not a palindrome')
    
    
    



def printTri2(se):
    for i in range(0, se):
        for j in range(0,i+1):
            print('*', end=" ")
        print()

def solution(h, n):
   for i in range(0,n):
       printTri2(h+i)


rows = int(input('enter value: '))
seg = int(input('enter value: ')) 
solution(rows, seg)


        
    



import math

L = [2,3,5,7,9,13]
left = 0
right = int(len(L) -1)

min1 = int(input("Enter a Left Number: "))
max1 = int(input("Enter a Right Number: "))

def binarySearch(L, left, right,min1,max1):
    #print("run")
    #print (half)
    mid = (left+right)//2
    print(mid)
    
    if L[mid] == min1:
        return True
    if L[mid] == max1:
        return True

    #if mid+1 >= len(L):
    #    return False

    if L[mid] < max1 and L[mid] > min1:
        return True
        

    if L[mid] < min1:
        return binarySearch(L,mid+1,right,min1,max1)

    if L[mid] > max1:
        return binarySearch(L,left,mid-1,min1,max1)

   

    return False
        
    
   


     
print (binarySearch(L,left, right,min1,max1))


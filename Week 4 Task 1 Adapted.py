import math

inOne = input("Enter a Number to search for: ")

L = [2,3,5,7,9,13]
left = 0
right = len(L)-1

def binarySearch(L, target, left, right):
    #print("run")
    #print (half)
    mid = (left+right)//2
    print(mid)
    
    if L[mid] == target:
        return True

    if mid+1 >= len(L):
        return False

    if L[mid] < target:
        return binarySearch(L,target,mid+1,right)

    if L[mid] > target:
        return binarySearch(L,target,left,mid-1)

   

    return False
        
    
   

x1 = int(inOne)
     
print (binarySearch(L, x1, left, right))


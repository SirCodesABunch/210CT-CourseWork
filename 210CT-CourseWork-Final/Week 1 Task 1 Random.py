import random

# The input of numbers
A = [5,3,8,6,1,9,2,7]
print ("Orginal" + str(A))
def shuffleList(A):

#Sets up a for loop that has the length of the input
    for i in range(len(A)):
        r = random.randint(0, 7)
#random number is generated each time the loop is run.
        swapping = A[i]
        swapping2 = A[r]
#setting up swapping variables
        listLength = len(A)
#making sure it does'nt go out of bounds
    
        if i > listLength:
            x = i-1
        else:
            x = i
#The actual swapping
        A[x] = swapping2
        A[r] = swapping

#Showing what it is doing.
        print ("Swapping " + str(x) + " With " + str(r))
        print ("Swapping " + str(swapping) + " With " + str(swapping2))
        print ("Stage " + str(i) + " " + str(A))
    print ("Fianl " + str(A))


# Running the function.
shuffleList(A)

#x, y = y, x

#tmp = x
#x = y
#y= tmp
        

    

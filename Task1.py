"""
A = 30
B = 6
C = 20
D = 10


def Compute(A,B,C,D):
    AB = A/B
    CD = C/D

    if AB > CD:
        print (AB)
        
    else:
        print (CD)
                
     

Compute(A,B,C,D)
"""
from math import sqrt


"""
a = (3,4)
a1 = (3)
a2 = (4)

b = (0,5)
b1 = 0
b2 = 5

c = (6,9)
c1 = 6
c2 = 9

gridPostionA1 = 0 
girdPostionA2 = 0
gridPostionB1 = 0
gridPostionB2 = 10
gridPostionC1 = 10
gridPostionC2 = 0
gridPostionD1 = 10
gridPostionD2 = 0
p = (-2,4)
postionA1 = -2
postionA2 = 4
origin = (0,0)

def calculate():
    DistanceAB = sqrt((a1**2+a2**2)+(b1**+b2**2))
    DistanceBC = sqrt((b1**2+b2**2)+(c1**2+c2**2))
    DistanceAC = sqrt((a1**2+a2**2)+(c1**2+c2**2))
    print (DistanceAB, DistanceBC, DistanceAC)
    
    #Left
    distanceGridAB = sqrt((0)+(gridPostionB1**2+gridPostionB2**2))
    #Bottom
    distanceGridAC = sqrt((0)+(gridPostionC1**2+gridPostionC2**2))
    #Top
    distanceGridBD = sqrt((gridPostionB1**2+gridPostionB2**2)+(gridPostionD1**2+gridPostionD2**2))
    #Right
    distanceGridCD = sqrt((gridPostionC1**2+gridPostionC2**2)+(gridPostionD1**2+gridPostionD2**2))
    print (distanceGridAB, distanceGridAC, distanceGridBD, distanceGridCD)

    postionDistance

    if 

    

        

calculate()
"""
def calculate(x):
    if x < -2:
        ans = x**2+4*x+4
        return(ans)
    elif x == 0:
        ans = 0
        return(ans)
    elif x > -2:
        ans = x**2+5*x
        return(ans)
    else:
        print ("ERROR")



x = input("Please enter a decimal number: ")

try:
    y = float(x)
    calculate(y)
    calResult = calculate(y)
    print ("Answer: " + str(calResult))

except TypeError:
    print("Close")








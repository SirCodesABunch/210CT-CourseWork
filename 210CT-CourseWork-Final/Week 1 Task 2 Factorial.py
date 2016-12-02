
x = input("Please enter a number: ")

b = int(x)

def factorial(n):
    
    
    c = 0
    times = []
    for i in range(n,0,-1):
        #Generates of a list of every number before n.
        times.append(i)
    '''
    for k in range(0,len(times)):
        if times[k] % 5 == 0:
            c = c + 1
    '''

    for m in range(1,len(times)-1):
        #Causes every element of the list to times with each other.
        times[0] = times[0] * times[m]


    ans = str(times[0])
    count = 0

    for c in range(len(ans)-1,0,-1):
        #Checks how many zeros are at the end.
        if ans[c] == "0":
            count = count + 1
        else:
            break
        
    print (ans)
    return str(n) + " Has " + str(count) + " Trailing Zero's"

    
        
        







print ( factorial(b))




x = input("Please enter a number: ")

b = int(x)

def factorial(n):

    cN = n

    bN = [n]

    while cN > 0:
        print (str(cN-1))
        cN = cN - 1
        bN.append(cN)
        

    acceptables = []

    i = 100
    while i > 0:
        a = i * 5
        i = i - 1
        acceptables.append(a)
        print (str(acceptables))

        
    count = 0
    if acceptables in bN:
            count = count + 1
    for pos in bN:
        bN[pos] = 0
        if acceptables in bN:
            count = count + 1

        else:
            break

    print (str(n) + " Has " + str(count) + " Zero's at the end")
        







factorial(b)



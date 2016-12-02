
i = input("Please enter a number: ")
x = int(i)

def primeCheck(n,c):

    if  c < 0:
        return ("This number is not prime")

    if c == 1:
        if n % c == 0:
            return (str(n) + " Is Prime!")

    if n % c == 0:
        return (str(n) + " Is NOT Prime!")

    

    return primeCheck(n,c-1)


print (primeCheck(x,x-1))

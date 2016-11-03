

x = input("Please Enter A Number: ")
n = float(x)
y = 2

def primeNumberChecker(n,c):

    if  n == 0:
        return (n + " Is NOT Prime!")

    if n == 1:
        return (n + " Is NOT Prime!")

    if n == c:
        return (n + "Is A Prime Number")

    else:

        if n%c != 0:
            return (primeNumberCheck(n,c+1)


ans = primeNumberChecker(n,y)

print (ans)


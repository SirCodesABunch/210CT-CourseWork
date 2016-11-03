

s = input("Please enter a string: ")
x = str(s)
c = 0

def devowelaify(s, c):


    vowels = ["a","e","i","o","u"]
    vowelsUPPER = ["A","E","I","O","U"]
    print(c)
    if s[c] in vowels:
        s = s.replace(s[c],"")

    if s[c] in vowelsUPPER:
        s = s.replace(s[c],"")

    if c+1 > len(s)-1:
        return (s)
    else:
        return devowelaify(s,c+1)


ans = devowelaify(x, c)


print(ans)

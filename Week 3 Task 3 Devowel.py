
i = input("Please enter a string: ")
s = str(i)

def devowel(s,c):
    vowels = ["a","e","i","o","u"]
    vowelsUPPER = ["A","E","I","O","U"]
    print (c)
    print (len(s))
    if c < 0:
        c = 0
    
    if s[c] in vowels:
        s = s.replace(s[c],"")
        if c+1 > len(s):
            return (s)
        else:
            return devowel(s,c-1)

    if s[c] in vowelsUPPER:
        s = s.replace(s[c],"")
        if c-1 > len(s):
            return (s)
        else:
            return devowel(s,c-1)

        
        return (s)

    



print(devowel(s,0))


s = input("Please enter a string: ")
x = str(s)

def devowelaify(s):


    vowels = ["a","e","i","o","u"]
    vowelsUPPER = ["A","E","I","O","U"]

    for i in range(len(s)-1):
        for c in range(len(vowels)-1):
            if s[i] == vowels[c]:
                s = s.replace(s[i],"")

            if s[i] == vowelsUPPER[c]:
                 s = s.replace(s[i],"")


    return (s)


ans = devowelaify(x)


print(ans)

        

        


        

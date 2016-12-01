i = input("Please enter a phrase: ")
x = str(i)

def wordReverse(p):

    words = p.split()
    newS = []
    print (words)

    for w in range(1,len(words)+1):
        print (-w)
        print (words[-w])
        newS.append(words[-w])

    return ' '.join(newS)

print (wordReverse(x))

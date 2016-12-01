
i = input("Please enter a string: ")
s = str(i)

def devowel(s,c):
    '''
    recursively goes through and removes all vowels from a given string.
    If the count variable is ever reduced to below 0 it gets set to 0.
    If the function goes over the length of the string OR the string is empty
    it terminates returning it's result.
    Checks if a letter of the string is in the etheir vowel list
    if it is it is removed and it runs the function again but back a space
    (This is because the entire string shuffled one backwards.)
    '''
    vowels = ["a","e","i","o","u"]
    vowelsUPPER = ["A","E","I","O","U"]
    #print (s)
    if c < 0:
        c = 0

    if c+1 > len(s) or s == None:
        return (s)
    
    
    if s[c] in vowels or s[c] in vowelsUPPER:
        s = s.replace(s[c],"")
        return devowel(s,c-1)
        
    

    return devowel(s,c+1)


    



print(devowel(s,0))

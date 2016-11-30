#7,1,3,4,1,1,2,6,7

l = [1,2,3,4,1,5,1,6,7]


def subList(l):

    c = 0
    store = []
    for j in range(0,len(l)):
        #Finds all the sublists and then places them in the 'store' list
        #The sublists are stored as positions and length of the sublist is also
        #store.

        if j+1 >= len(l):
            print ("//Reached the end of the list!//")
            t = [j+1 , c+1]
            store.append(t)
            c = 0
            break

        if l[j] < l[j+1]:
            c = c+1
            print ("//Still a sublist//")
            
            continue

        print ("//No longer a sublist. Adding to store//")

        t = [j+1 , c+1]
        store.append(t)
        c = 0

    print (store)

    current = 0
    

    for i in range(0,len(store)):
        #Compares each sublist to eachother to find out which is the longest.
        if i+1 > len(store):
                break

        for j in range(1,len(store)):
            if j+1 > len(store):
                break
            if store[i] == store[j]:
                continue
            
            elif store[i][1] > store[j][1]:
                current = store[i]
            else:
                current = store[j]

    print (current)
    subList = []
    for a in range(0,current[1]):
        #Prints out the sublist of longest length
        if a+1 > len(l):
                break

        subList.append(l[(current[0] -1) - a])
        print(l[(current[0] -1) - a])

    #just to display it in order check if this is OK?
    subList.sort()
    print(subList)

   
        
        
subList(l)

                

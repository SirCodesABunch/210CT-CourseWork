#7,1,3,4,1,1,2,6,7

l = [7,1,3,4,1,1,2,6,7]


def subList(l):
    #Start Search
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
    #END OF Search

    #print (store)

    current = None

    for i in range(0,len(store)):
        #Compares each sublist to eachother to find out which is the longest.
        #Outer loop marks one of the total length's of the sublists
        #The inner loop then compares the other sublists length to that one node
        #Every sublist's length is compared with every other sublist's length.
        if i+1 > len(store):
                break

        for j in range(0,len(store)):
            if j+1 > len(store):
                break
            if store[i] == store[j]:
                #Checks if the sublist is looking at itself if it is skips to next
                continue

            elif store [i][1] == store[j][1]:
                #If they are both the same length AND they are bigger than the highest current.
                #Both of them will be added
                if current == None or current[1] < store[i][1]:
                    current = store[i].append(store[j][0])
                    current = store[i].append(store[j][1])
                    
            #this part compares the i's total length to j's total length.
            #it then checks if the highest total length is less than i's or j's
            #if etheir is bigger it replaces the current highest with the value of i's or j's length.
            elif store[i][1] > store[j][1]:
                
                if current == None or current[1] < store[i][1]:
                    current = store[i]
            else:
                if current == None or current[1] < store[j][1]:
                    current = store[j]

    print (current)
    subList = []
    temp = []

    #Checks to see if there is more than one sublists of longest length.
    if len(current) == 2:
        for a in range(0,current[1]):
            #Prints out the sublist of longest length
            if a+1 > len(l):
                    break

            subList.append(l[(current[0] -1) - a])
            print(l[(current[0] -1) - a])
            subList.sort()

    else:
        #Here i is the position that the sublist ends on.
        for i in range(0,len(current),2):
            for a in range(0,current[1]):
                #Current[i] is the position that the sublist ends on the -1 is there to point it to the last
                #element in the sublist
                #runs and goes back through the sublist based on the total length of the sublist stored in current[1]
                temp.append(l[(current[i]-1) - a])
                temp.sort()
                #print ("pre " + str(temp))
            subList.append(temp)
            temp = []

    
    return(subList)

   
        
        
print (subList(l))

                

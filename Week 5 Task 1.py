
l = [7,1,3,4,1,1,2,6,7]


def subList(l):

    c = 0
    store = []
    for j in range(0,len(l)):

        if j+1 >= len(l)-1:
            print ("//Reached the end of the list!//")
            t = [j+1 , c+1]
            store.append(t)
            c = 0
            break

        if l[j] < l[j+1]:
            c = c+1
            print ("//Bump//")
            
            continue

        print ("//Adding to store//End of Loop//")

        t = [j+1 , c+1]
        store.append(t)
        c = 0

    print (store)

    current = 0
    

    for i in range(0,len(store)):

        if store[i [1]] > store[i+1[1]]:
            current = store[i]
        else:
            current = store[i+1]

    return current

    

    

    





    return store

        
        
print (subList(l))

                

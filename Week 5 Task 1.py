
l = [7,1,3,4,1,1,2,6,7]


def subList(l):


    store = [0]
    for i in range(0,len(l)):
        c = i

        for j in range(c,len(l)):

            if j == len(l)-1:
                print ("//Reached the end of the list!//")
                #store.append(j)
                break
            

            if j+1 > len(l)-1:
                print ("//Reached the end of the list!//")
                store.append(j)
                break

            if l[j] < l[j+1]:
                print ("//Bump//")
                continue

            print ("//Adding to store//End of Loop//")

            store.append(j+1)

    print (store)

    compare = []

    for x in range(0,len(store)):

        if x+1 > len(store)-1 or x > len(store)-1:
            break
        
        f = range(store[x],store[x+1])
        if len(f) > len(compare):
            compare = list(f)


    for a in range(0,len(compare)):

        if a+1 > len(compare)-1:
            compare[a] = l[compare[a]]
            break

        compare[a] = l[compare[a]]
    
    return (compare)


        
        
print (subList(l))

                

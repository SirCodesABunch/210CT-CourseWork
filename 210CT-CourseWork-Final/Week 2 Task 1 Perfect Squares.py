def PerfectSquare(N):


        #perfectSquareList = [0]
        #listCount = 0   
        count = 0
        currentHighest = None

        while count < N:
                count =  count + 1
                X =  count * count
                print(str(X), str(count))
            
                if X <= N:
                        currentHighest = str(count) + "*" + str(count)

                elif X > N:
                        if currentHighest != None:
                                return currentHighest
                        else:
                                return "ERROR"


print (PerfectSquare(1))

#a = PerfectSquare(41)


def PerfectSquare(N):


	perfectSquareList = [0]
	listCount = 0	
	count = 0

	while count < N:
		count =  count + 1
		X =  count * count

		print(str(X), str(count))
	    
	if X == N:
		return X

	elif X < N:
		perfectSquareList.append(X) 
		listCount = listCount + 1
		print (str(x) + " Added to List!") 
		
	

	last = len(perfectSquareList)

	return perfectSquareList[last-1]

print (PerfectSquare(26))

a = PerfectSquare(41)


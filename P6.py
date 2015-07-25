# Finds the difference between the sum of the squares of the first given 
# number of natural numbers and the square of the sum

def square(x):
	return x * x

def P6(x):
	ls = range(1,x + 1)
	diff = sum(ls)**2 - sum(map (square, ls))
	return diff
	
print P6(10) #2640
print P6(100) #25164150
# Find the smallest common multiples of integers from 1 to x
# Possible improvements, only test for prime numbers
# Make a list of prime
# and instead of d += 1, uses prime[d+=1], using index to call the prime

def P5(x):
	d = 1
	y = 1
	while d <= x:
		if (y % d == 0):
			d += 1
		else:
			d = 1
			y += 1
	return y

print P5(10) #2520
print P5(20) #232792560
# looking for the nth prime

def P7(n): 
	pli = [2] # a list to store the prime numbers
	i = 0 # list index
	x = pli[i] # the incrementing number which the loop will check if it is Prime
	while((i + 1) < n):
		x += 1
		if (isPrime(x,pli,i)): #
			i += 1 # increment the index
			pli.append(x) # add the new prime number to list
			x += 1
	return pli[i]

def isPrime(n,pli,i):
	j = 0
	while j <= i: # walk through the pli to see if n can be factored by any element
		if (n % pli[j]) == 0:
			return False
		else:
			j += 1
	return True # if n cannot be factored by any prime number, it is prime

# Consider using the fact that prime number are in the form
# 6n + 1 or 6n - 1 after 2, 3 to improve performance.

# print P7(1)
# print P7(2)
# print P7(3)
# print P7(4)
# print P7(5)
# print P7(6)
# print P7(7)
# print P7(8)
# print P7(9)
# print P7(10)
print P7(10001) # 104743


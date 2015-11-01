#Find the sum of all the primes below n (in this case, two million).
#from math import sum
#Sieve of Eratosthenes
def P10(n):
	primes = range(3,n+1,2)
	primes = [2] + primes
	#print primes
	i = 1 # the composites of 2 have been removed by construction
	while (i < len(primes)):
		if i**2 > n:
			return sum(primes)
		f = primes[i]
		j = i + 1
		while (j < len(primes)):
			if (primes[j] % f) == 0:
				#print 'del'
				#print primes[j]
				del primes[j]
				j -= 1
				# after the compsite is deleted, the index of the later 
				# elements is subtracted by one
			j += 1 # move along the list
		i += 1
	return sum(primes) 

#Slow way:
#def P10(n):
#	pli = [2,3] # list of primes
#	i = 1 # current index of list
#	sum = 5 # sum of the elements in list
#	for x in range(5,n+1,2):
#		if (isPrime(x,pli,i)):
#			i += 1
#			pli.append(x)
#			sum += x
#			print x
#	return sum

#def isPrime(n,pli,i):
#	j = 0
#	while j <= i:
#		if (n % pli[j]) == 0:
#			return False
#		else:
#			j += 1
#	return True

#print P10(7) # 17
#print P10(100000) # 454396537
print P10(2000000) #142913828922

#####



# Find the nth prime number

# def P7(x):
# 	ls = [2]
# 	n = 2
# 	index = 0
# 	while len(ls) != x:
# 		while (n%(ls[index])) == 0:
# 			n += 1
# 		if len(ls) == (index + 1):
# 			ls.append(n)
# 			index = 0
# 		else:
# 			index += 1

# 	return (ls[len(ls)-1])

#if a%n == 0:
#			n += 1
#			i += 1
#		else:
#			a += 1	


# def isPrime(n):
# 	if (n % 2) == 0:
# 		return 1
# 	if (n % 3) == 0:
# 		return 2
# 	i = 6;
# 	count = 3
# 	while (true):
# 		if (n % (i - 1)) == 0:
# 			return count
# 		else:
# 			count += 1
# 		if (n % (i + 1)) == 0:
# 			return count
# 		else:
# 			count += 1

# def P7(n): # looking for the nth prime
# 	count = 1
# 	p = 2
# 	x = 0
# 	while(count < n):
# 		p += 1
# 		if (isPrime(p,x)):
# 			count += 1
# 			x = p
# 	return p
	

# # Takes advantage of the fact that a prime number is in the form
# # of 6n + 1  or 6n - 1 after 2 and 3
# # x is the preceding prime number
# def isPrime(n, x):
# 	if n == 2:
# 		return True
# 	if n == 3:
# 		return True
# 	if (n % 2) == 0:
# 		return False
# 	if (n % 3) == 0:
# 		return False
# 	if x < 5:
# 		i = 5
# 	elif ((x + 1) % 6) == 0:
# 		i = x + 1
# 	else:
# 		i = x - 1
# 	while (i != n): 
# 		i -= 1
# 		if (i == n):
# 			return True
# 		if (n % i) == 0:
# 			return False
# 		i += 2 # incorrect for isPrime(25,23)
# 		if (i == n): # 25 == 25
# 			return True
# 		if (n % i) == 0:
# 			return False
# 		i = i - 1 + 6
# 	return True

def P7(n): # looking for the nth prime
	i = 0
	pli = [2] # a list to store the prime number
	x = pli[i]
	while((i + 1) < n):
		x += 1
		if (isPrime(x,pli,i)): # 
			i += 1
			pli.append(x)
			x += 1
	return pli[i]

def isPrime(n,pli,i):
	j = 0
	while j <= i:
		if (n % pli[j]) == 0:
			return False
		else:
			j += 1
	return True

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


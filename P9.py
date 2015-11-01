#Given a + b + c = 1000 and a^2 + b^2 = c^2
#Find a*b*c

from math import sqrt

#Slow idea:
#Skip if a + b + c != 1000
#Test all possibility of i, j, k in three loops
# i^2 j^2 == k^2
# print all three values and exit loop

def P9(x):
	for i in range(1,998):
		for j in range(1,998):
			for k in range(1,998):
				if (i + j + k == x):
					if (i ** 2 + j ** 2 == k ** 2):
						print i
						print j
						print k
						return i*j*k
print P9(1000) #31875000

########
# Faster Idea
# In a list of odd number choose a perfect square
# that number will be a^2, and the nth number in the sequence
# n = (a^2 + 1)/2
# then sum all the previous number, that'll be b^2
# and add the current number, that'll be c^2



#def P9(x):
#	for AS in range(1, 1000000, 2): # an odd number sequence
#		a = sqrt(AS)
#		if a.is_integer(): # check if the current AS is a perfect square
#			a = int(a)
#			n = (AS + 1)/2
#			b = n - 1
#			c = n
#			if (a + b + c == x):
#				return a*b*c
#				break

#isinstance(a, int): 

#Given the 20 x 20 grid
#Find the greatest product of four adjacnet numbers in the same direction

#Represent the grid in a matrix
M = [[8,02,22,97,38,15,0,40,0,75,04,05,07,78,52,12,50,77,91,8],
[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,04,56,62,00],
[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,03,49,13,36,65],
[52,70,95,23,04,60,11,42,69,24,68,56,01,32,56,71,37,02,36,91],
[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
[24,47,32,60,99,03,45,02,44,75,33,53,78,36,84,20,35,17,12,50],
[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
[67,26,20,68,02,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
[24,55,58,05,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
[21,36,23,9,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95],
[78,17,53,28,22,75,31,67,15,94,03,80,04,62,16,14,9,53,56,92],
[16,39,05,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57],
[86,56,00,48,35,71,89,07,05,44,44,37,44,60,21,58,51,54,17,58],
[19,80,81,68,05,94,47,69,28,73,92,13,86,52,17,77,04,89,55,40],
[04,52,8,83,97,35,99,16,07,97,57,32,16,26,26,79,33,27,98,66],
[88,36,68,87,57,62,20,72,03,46,33,67,46,55,12,32,63,93,53,69],
[04,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,04,36,16],
[20,73,35,29,78,31,90,01,74,31,49,71,48,86,81,16,23,57,05,54],
[01,70,54,71,83,51,54,69,16,92,33,48,61,43,52,01,89,19,67,48]]

#Compute the greatest product for horizontal direction

def hp(m,r,c):
	rv = 0
	for row in M: # in the first run, row[0] = 08
		for col in range (0,c-3):
			p = row[col] * row[col+1] * row[col+2] * row[col+3]
			if p > rv:
				rv = p	
	return rv
#print hp(M,20,20)

#Compute the greatest product for vertical direction

def vp(m,r,c):
	rv = 0
	n = [[row[i] for row in m] for i in range(c)] # transpose
	return hp(n,c,r)

#Compute the greatest product for diagonal (top left to bottom right) direction

def dp1(m,r,c):
	rv = 0
	for row in range(0,r-3):
		for col in range(0,c-3):
			p = m[row][col] * m[row+1][col+1] * m[row+2][col+2] * m[row+3][col+3]
			if p > rv:
				rv = p
	return rv

#Compute the greatest product for diagonal (bottom left to top right) direction
def dp2(m,r,c):
	rv = 0
	for row in range(3,r):
		for col in range(0,c-3):
			p = m[row][col] * m[row-1][col+1] * m[row-2][col+2] * m[row-3][col+3]
			if p > rv:
				rv = p
	return rv

#Combine them
#Generalize the function to n x m, with each > 4.

def P11(M):
	r = len(M)
	c = len(M[0])
	if (r < 4) or (c < 4):
		return "The input must be an n x m matrix with n > 4 and m > 4"
	return max(hp(M,r,c), vp(M,r,c), dp1(M,r,c), dp2(M,r,c))

print P11(M) #70600674

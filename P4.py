def P4(o):
	x, y = 999, 999
	z = x * y
	while (str(z) != str(z)[::-1]):
		if (x - y > 100):
			x -= 1
			y = x
		else:
			y -= 1
		z = x * y
	print z
P4(0) #906609
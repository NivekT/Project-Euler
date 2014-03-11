#Created by Kevin T.
#Finds the sum of the even-valued terms of the Fibonacci sequence, whose terms do not exceed the input n.

def fib(n):
    x, y, s = 0, 1, 0
    while y < n:
        if (y%2 == 0):
            s = s + y
            print s
        x, y = y, x+y
    

#Created by Kevin T.
#Finds the sum of all the multiples of 3 or 5 below the input n.

def EU1(n):
    x, s = 0, 0
    while (x < n):
        if x % 3 == 0:
            s = s + x
        elif x % 5 == 0:
            s = s + x
        x = x + 1
    print s

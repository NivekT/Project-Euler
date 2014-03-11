#Created Kevin T.
#Finds the largest prime factor of the input x.

def EU3(x):
    f = 2
    while x%f != 0:
        f = f + 1
    while x%f == 0:
            x = x/f
            while x%f != 0:
                if x == 1:
                    break
                f = f + 1              
    print f


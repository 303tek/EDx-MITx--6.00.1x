def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code
    sInt=min(a,b)
    for i in range(sInt,0,-1):
        if (a % i == 0 and b % i == 0):
            break
    return(i)

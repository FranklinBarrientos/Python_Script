def myLog(x, b):
    '''
	test
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if b >x:
        return 0
    else:
        return 1+myLog(x/b, b)       
    
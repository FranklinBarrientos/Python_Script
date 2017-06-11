def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    

def radiationExposure(start, stop, step):
    A=0
    while start!=stop:
        A+=step*f(start)
        start+=step
    return A
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    

def radiationExposure(start, stop, step):
    
    if abs(start-stop)<=step:
        return step*f(start)    
    else:        
        return step*f(start)+radiationExposure(start+step, stop, step)
def recurPower(base, exp):

    if exp==0:
            return 1
    elif exp%2 == 1:
        return base*recurPower(base, exp-1)
    else:
        return recurPower(base*base, exp/2) 

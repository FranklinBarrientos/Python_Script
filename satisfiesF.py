def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    newList = [k for k in L if f(k) == True]
    L[:] = newList     
    return len(L)

run_satisfiesF(L, satisfiesF)
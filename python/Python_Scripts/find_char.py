def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid=len(aStr)
    
    if mid==0:
        return False
    
    elif aStr[mid/2]==char:
        return True
    
    elif aStr[mid/2]<char:
        aStr=aStr[mid/2+1:mid]
        
    elif aStr[mid/2]>char:
        aStr=aStr[0:mid/2]
    
    return isIn(char,aStr)

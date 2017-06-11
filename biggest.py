def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    Min=0
    if len(aDict)==0:
        return None
    else:
        for i in aDict.keys(): 
            print i
            if Min<=len(aDict[i]):
                Min=len(aDict[i])
                key=i
        return key



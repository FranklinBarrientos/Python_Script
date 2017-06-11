def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    if len(aDict)!=0:
        return sorted([i for i in aDict.keys() if aDict[i]==target]) 
    else:
        return []
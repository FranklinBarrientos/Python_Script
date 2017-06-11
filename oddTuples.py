def oddTuples(aTup):
    
    if len(aTup)<1:
        return ()
    else:
        return (aTup[0],)+oddTuples(aTup[2:])
    
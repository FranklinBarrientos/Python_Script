def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    copy=hand.copy()
    if word in wordList:
        for i in word:
           if i in copy:
                copy[i]=copy[i]-1
                if copy[i]==0:
                    return False
           else:
               return False
        return True                 
    else:
        return False
        
        
    #el codigo de abajo no se me ocurrio :(    
    #word_as_dict = getFrequencyDict(word)
    #return word in wordList and all(item[0] in hand.keys() 
                                #and hand[item[0]] >= item[1] 
                                #for item in word_as_dict.items())

#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    
    if secretWord=='':
        return True
    else:
        return (secretWord[0] in lettersGuessed) and isWordGuessed(secretWord[1:], lettersGuessed)


   
   
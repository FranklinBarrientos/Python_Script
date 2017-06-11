# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/PROPIETARIO/Desktop/Script_Python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if secretWord=='':
        return True
    else:
        return (secretWord[0] in lettersGuessed) and isWordGuessed(secretWord[1:], lettersGuessed)




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if secretWord=='':
        return ''  
    else:
        Boolop=secretWord[0] in lettersGuessed
        strg=(not Boolop and '_')or(Boolop and secretWord[0])
        return strg+getGuessedWord(secretWord[1:], lettersGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    cadena=string.ascii_lowercase
     
    for i in lettersGuessed:
        j=0
        while True:  
            if i == cadena[j]:
                cadena=cadena[:j]+cadena[j+1:]
                break
            j+=1    
    return cadena
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed_loop=[]
    num_chance=8
    print 
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
     
    #Loop-function    
    while True:
        print
            
        print('You have '+str(num_chance)+' guesses left.')  
        print('Avaible letters: '+ getAvailableLetters(lettersGuessed_loop)), 
        lettersGuessed=str(raw_input('Please guess a letter: '))
     
                           
        if lettersGuessed in lettersGuessed_loop:   
            print("Oops! You've already guessed that letter:"+ getGuessedWord(secretWord, lettersGuessed_loop))

    
        elif lettersGuessed in secretWord:
            lettersGuessed_loop=lettersGuessed_loop+[lettersGuessed]
            print('Good guess: '+ getGuessedWord(secretWord, lettersGuessed_loop))
       
        elif not (lettersGuessed in secretWord): 
            lettersGuessed_loop=lettersGuessed_loop+[lettersGuessed]  
            print('Oops! That letter is not in my word:'+ getGuessedWord(secretWord, lettersGuessed_loop))
            num_chance-=1

        if secretWord!=getGuessedWord(secretWord, lettersGuessed_loop) and num_chance==0:
            print ('Sorry, you ran out of guesses. The word was else.')
            break
            
        elif secretWord==getGuessedWord(secretWord, lettersGuessed_loop) and num_chance!=0:
            print('Congratualtions, you won')            
            break
            
            
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

def getAvailableLetters(lettersGuessed):
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
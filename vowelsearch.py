char='I'

def vowel(char):
    
    test='aeiouAEIOU'

    for i in test:  
          
        if char == i:
            print True
            break
        elif i == test[9]:         
            print False
            
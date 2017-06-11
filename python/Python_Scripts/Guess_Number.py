
x = 100
epsilon = 0.5
numGuesses = 0
low = 0.0
high = x
ans = int((high + low)/2.0)

print "Please think of a number between 0 and 100!"

while abs(ans - x) >= epsilon:
    print('Is your secret number ' + str(ans) + '?')
    guess=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    numGuesses += 1
    if guess == 'h':
        high = ans
    elif guess == 'l':
        low = ans
    elif guess == 'c':
        print('Game over. Your secret number was: ' + str(ans))
        break
    else:
        print('Sorry, I did not understand your input.')
    ans = int((high + low)/2.0)

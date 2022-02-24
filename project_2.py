def refreshHangman():
    hangman = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ]
    return hangman

def drawHangman(hangman):
    for i in range(8):
        for j in range(10):
            print(hangman[i][j], end="")
        print("", end='\n')

def drawHead(hangman):
    hangman[2][7] = 'O'
    return hangman

def drawBody(hangman):
    hangman[3][7] = '|'
    hangman[4][7] = '|'
    return hangman

def drawLeftArm(hangman):
    hangman[3][6] = '\\'
    return hangman

def drawRightArm(hangman):
    hangman[3][8] = '/'
    return hangman

def drawLeftLeg(hangman):
    hangman[5][6] = '/'
    return hangman

def drawRightLeg(hangman):
    hangman[5][8] = '\\'
    return hangman

def drawNoose(hangman):
    hangman[1][7] = '|'
    return hangman

def printGuess(guess):
    for entry in guess:
        print(entry, end=' ')
    print('\n')

### MAIN ###

# Ask player 1 to input a word
answer = input('Player 1 please enter a word: ')
answer = answer.upper()
print(chr(27) + "[2J")

print('Player 2, you are guessing a ' + str(len(answer)) + '-letter word.')

# Initialize game parameters
guess = ['_']*len(answer)   # Player 2's guess
guessedLetters = []         # Letters guessed by Player 2
missed = 0                  # Total number of missed guesses
hangman = refreshHangman()  # Initialize the Hangman drawing

# Start the game play.
while '_' in guess and missed < 7:
    letter = input('Player 2, please guess a letter: ').upper()

    # Clear the screen
    print(chr(27) + "[2J")

    # Error check
    if len(list(letter)) != 1:
        print('Please enter one letter and one letter only!')
        continue
    elif not letter.isalpha():
        print('Please enter a letter!')
        continue
    else:
        indices = [index for index, element in enumerate(
            answer) if element == letter]

        if letter not in guessedLetters:
            guessedLetters.append(letter)
            guessedLetters.sort()

        if len(indices) == 0:
            missed += 1
            if missed == 1:
                hangman = drawHead(hangman)
            elif missed == 2:
                hangmang = drawBody(hangman)
            elif missed == 3:
                hangman = drawLeftArm(hangman)
            elif missed == 4:
                hangman = drawRightArm(hangman)
            elif missed == 5:
                hangman = drawLeftLeg(hangman)
            elif missed == 6:
                hangman = drawRightLeg(hangman)
            else:
                hangman = drawNoose(hangman)
        else:
            for i in indices:
                guess[i] = letter

        print('Your current answer is: ')
        printGuess(guess)
        print('You have guessed these letters: ')
        printGuess(guessedLetters)
        drawHangman(hangman)

# Determine the final outcome of the play
if missed == 7:
    print('YOU LOST!')
    print('THE CORRECT ANSWER IS:')
    printGuess(answer)
else:
    print('CONGRATULATION!')
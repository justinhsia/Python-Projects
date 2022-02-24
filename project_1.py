'''
Project 1: Connect Four
Student: Justin
'''

def drawField(currentField):
    '''
    Draw the game field of 6 x 7 slots.
    
    ---------------
    | | | | | | | |
    ---------------
    | | | | | | | |
    ---------------  
    | | | | | | | |
    ---------------
    | | | | | | | |
    --------------- 
    | | | | | | | |
    ---------------
    | | | | | | | |
    --------------- 
    
    '''
    
    for row in range(13):
        if row%2 == 0:
            print('---------------')
        else:
            for col in range(15):
                if col%2 == 0:
                    if col == 14:
                        print('|')
                    else:
                        print('|', end='')
                else:
                    print(currentField[(col-1)//2][(row-1)//2], end='')

def isNotFilled(currentField, moveCol):
    '''
    This function is a utility function that will be called by other functions.
    This function check to see if the current cell is filled already or not.
    '''
    return currentField[moveCol-1][0] == ' '

def checkWin(vector):
    '''
    This function is a utility function, which will be called by other functions.
    This function will check to see if the input vector contains the winning
    pattern.
    '''

    symbol = ' '
    counter = 0

    for index in range(len(vector)):
        if vector[index] != ' ':
            if symbol == vector[index]:
                counter += 1
                if counter == 4:
                    break
            else:
                symbol = vector[index]
                counter = 1

    if counter == 4:
        return True
    else:
        return False

def rowWin(currentField, row, col):
    '''
    This function checks to see if the input row vector contains the 
    winning pattern.
    '''
    rowVector = [l[row] for l in currentField]
    return checkWin(rowVector)

def colWin(currentField, row, col):
    '''
    This function checks to see if the input column vector contains
    the winning pattern.
    '''
    colVector = currentField[col]
    return checkWin(colVector)

def diagWin(currentField, row, col):
    '''
    This function checks to see if the input diagonal vector contains the
    winning pattern.
    '''
    if row >= col:
        row -= col
        col = 0
        diagVector = [currentField[col+i][row+i] for i in range(6-row)]
    else:
        col -= row
        row = 0
        diagVector = [currentField[col+i][row+i] for i in range(7-col)]
    return checkWin(diagVector)

def antiDiagWin(currentField, row, col):
    '''
    This function checks to see if the input anti-diagonal vector contains
    the winning pattern.
    '''
    if (5-row) >= col:
        row += col
        col = 0
        antiDiagVector = [currentField[col+i][row-i] for i in range(row+1)]
    else:
        col -= (5-row)
        row = 5
        antiDiagVector = [currentField[col+i][row-i] for i in range(7-col)]
    return checkWin(antiDiagVector)

def checkGameWon(currentField, row, col):
    '''
    After a play is made, this function will be called to check to see
    if there is a winning pattern on the field.  Each of the four "Win"
    functions (rowWin, colWin, diagWin, antiDiagWin) will be called to
    check for winning pattern.
    '''
    if rowWin(currentField, row, col) or colWin(currentField, row, col) \
    or diagWin(currentField, row, col) or antiDiagWin(currentField, row, col):
        return True
    else:
        return False

### MAIN ###
'''
This is the main part of the program.  It first initialize the the play field
to contain 6 x 7 empty squares.  It assigns player one chip to '0' and player
two chip to 'X'.  Then it enters a while loop to start running the game.

Input error checking is built into this part of the program to make sure only
legal inputs are accepted.  Illegal inputs will cause the program to prompt the
user to re-enter another input until a valid input is received.

Whether a winning pattern is present is checked on every move.  If a winning
is detected, the game will exit out of the while loop and a loser will be 
declared.
'''
red = '0'
black = 'X'

player = 1

currentField = [[' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ']
               ]

drawField(currentField)

while True:
    
    while True:
        try:
            moveCol = int(input('Select an available column to place your chip: '))
            if moveCol >= 1 and moveCol <= 7 and isNotFilled(currentField, moveCol):
                break
        except ValueError:
            print('Please enter an integer.')
        except Exception as e:
            print('Enconter other errors: ' + str(e))
            print('Please enter a valid number.')

    if player == 1:
        # move for player 1
        rowIndex = 5
        isFilled = (currentField[moveCol-1][rowIndex] != ' ')
        
        while isFilled:
            rowIndex -= 1
            isFilled = (currentField[moveCol-1][rowIndex] != ' ')
        
        currentField[moveCol-1][rowIndex] = red
        
        player = 2
        
    else:
        # move for player 2 
        
        rowIndex = 5
        isFilled = (currentField[moveCol-1][rowIndex] != ' ')
        
        while isFilled:
            rowIndex -= 1
            isFilled = (currentField[moveCol-1][rowIndex] != ' ')
        
        currentField[moveCol-1][rowIndex] = black
        
        player = 1
        
    drawField(currentField)
    print('\n')
    
    # Check if someone wins.  If true, break.
    if checkGameWon(currentField, rowIndex, moveCol-1):
        print('Player ' + str(player) + ' has lost!')
        break

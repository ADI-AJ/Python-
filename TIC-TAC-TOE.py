theBoard = {'L1': ' ', 'L2': ' ', 'L3': ' ',
            'L4': ' ', 'L5': ' ', 'L6': ' ',
            'L7': ' ', 'L8': ' ', 'L9': ' '}
def printBoard(board):
    print(board['L1'] + '|' + board['L2'] + '|' + board['L3'])
    print('-+-+-')
    print(board['L4'] + '|' + board['L5'] + '|' + board['L6'])
    print('-+-+-')
    print(board['L7'] + '|' + board['L8'] + '|' + board['L9'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    print('top layer = L1,M1,R1 ; mid layer = L2,M2,M2 ; bottom layer = L3,M3,R3')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

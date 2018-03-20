"""TicTacToe using numpy"""
import numpy as np

# Initialize empty board
board = np.zeros([3, 3])


# recalculate sum in all directions to get status of game
def boardsum(board):
    return [
        *np.sum(board, axis=0),
        *np.sum(board, axis=1),
        np.sum(np.diag(board)),
        np.sum([board[0, 2], board[1, 1], board[2, 0]]),
    ]


# change player according to this boolean
one = False

# initialize boardsum
sums = boardsum(board)


# Get input field
# Has to be constrained -- TODO IMPLEMENT ME
def get_field():
    try:
        x = int(input('Choose row: ')) - 1
        y = int(input('Choose column: ')) - 1
        print('')
    except Exception as e:
        print('!!! Please insert numbers !!!')
        get_field()

    if x < 0 or x > 2 or y < 0 or y > 2:
        print('!!! Please choose valid field !!!')
        get_field()
    return x, y


def apply_update(x, y):
    # apply update to board - set mark
    if board[x, y] == 0:
        board[x, y] = num
    else:
        print('!!! Field already chosen !!!')
        apply_update(*get_field())


# repeat until finished or board is full
print('TicTacToe\n=========')
rounds = 1
while 3 not in sums and -3 not in sums and rounds <= 9:
    rounds += 1
    # change players with every turn
    if one:
        one = False
        num = -1
    else:
        one = True
        num = 1
    print('\n--------------------')
    print('It`s player {}s turn\n'.format(num))

    apply_update(*get_field())

    # recalculate sum
    sums = boardsum(board)

    print(board)

else:
    print('\nGame over\n')
    print(board)
    print('\n=============')
    print('Player {} won!'.format(num))
    print('=============')

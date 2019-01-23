
import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '
           }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def win_condition(Board):
    if Board['top-L'] != " " and Board['top-L'] == Board['top-M'] and Board['top-M'] == Board['top-R']:
        return True
    elif Board['mid-L'] != " " and Board['mid-L'] == theBoard['mid-M'] and Board['mid-M'] == Board['mid-R']:
          return True
    elif Board['low-L'] != " " and Board['low-L'] == Board['low-M'] and Board['low-M'] == Board['low-R']:
          return True
    elif Board['top-L'] != " " and Board['top-L'] == Board['mid-L'] and Board['mid-L'] == Board['low-L']:
          return True
    elif Board['top-M'] != " " and Board['top-M'] == Board['mid-M'] and Board['mid-M'] == Board['low-M']:
          return True
    elif Board['top-R'] != " " and Board['top-R'] == Board['mid-R'] and Board['mid-R'] == Board['low-R']:
          return True
    elif Board['top-L'] != " " and Board['top-L'] == Board['mid-M'] and Board['mid-M'] == Board['low-R']:
          return True
    elif Board['low-L'] != " " and Board['low-L'] == Board['mid-M'] and Board['mid-M'] == Board['top-R']:
          return True
    else:
        return False

def main():
    position = list(theBoard.keys())
    random.shuffle(position)
    turn = 'X'
    for i in range(len(position)):
        printBoard(theBoard)
        print("\nThe %d step"%(i+1))
        theBoard[position[i]] = turn
        if win_condition(theBoard):
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)
    print("\nGame Over")

if __name__ == "__main__":
    main()




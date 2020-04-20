import numpy

board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1='x'
p2='o'

def rows(symbol):
    for i in range(3):
        count=0
        for j in range(3):
            if(board[i][j]==symbol):
                count=count+1
        if (count==3):
            print(symbol," wins")
            return 1
        return 0

def cols(symbol):
    for j in range(3):
        count=0
        for i in range(3):
            if(board[i][j]==symbol):
                count=count+1
        if (count==3):
            print(symbol," wins")
            return 1
    return 0



def diags(symbol):
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol):
        print(symbol," wins")
        return 1
    if (board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol):
        print(symbol," wins")
        return 1
    return 0
def win(symbol):
    return rows(symbol) or cols(symbol) or diags(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row no. 1, 2 or 3 "))
        col=int(input("Enter column no. 1, 2 or 3 "))
        if (row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_'):
            break
        else:
            print("Invalid input")
    board[row-1][col-1]=symbol


def play():
    for turn in range(9):
        if(turn%2==0):
            print("x's turn")
            place(p1)
            if(win(p1)):
                break

        else:
            print("o's turn")
            place(p2)
            if(win(p2)):
                break

    if not(win(p1)) and not(win(p2)):
            print("Draw")
            print(numpy.matrix(board))

print("\t \t \t TIC-TAC-TOE GAME")
play()
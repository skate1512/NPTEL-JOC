# Rock-Paper-Scissors Game
""" This is a code for this game, player 1 selects a no. from which they select a digit this digit corresponds
to the value 0, 1 and 2.The same process is repeated with player 2. With the help of dictionaries, player 1 and 2
are shown the keys(0,1,2) which have different values assigned to them. Their choice results in a draw, victory or defeat.
An option to play again is provided. """


def rps(n1,n2,x,y):
    p1=int(n1[x])%3
    p2=int(n2[y])%3
    if (player1[p1]==player2[p2]):
        print("Draw")

    elif (player1[p1]=="Rock" and player2[p2]=="Paper"):
        print("Player 2 wins")
    elif (player1[p1]=="Rock" and player2[p2]=="Scissors"):
        print("Player 1 wins")
    elif (player1[p1]=="Paper" and player2[p2]=="Rock"):
        print("Player 1 wins")
    elif (player1[p1]=="Paper" and player2[p2]=="Scissors"):
        print("Player 2 wins")
    elif (player1[p1]=="Scissors" and player2[p2]=="Rock"):
        print("Player 2 wins")
    elif (player1[p1]=="Scissors" and player2[p2]=="Paper"):
        print("Player 1 wins")


player1={0:"Rock",1:"Scissors",2:"Paper"}
player2={0:"Scissors",1:"Paper",2:"Rock"}

print("Rock-Paper-Scissors Game")
while(1):

    num1=input("Player 1 enter  your random no.")
    num2=input("Player 2 enter  your random no.")
    a=int(input("Player 1 enter your game choice"))
    b=int(input("Player 2 enter your game choice"))
    rps(num1,num2,a,b)
    ch=input("Do you want to continue y/n:")
    if (ch=='n'):
        break

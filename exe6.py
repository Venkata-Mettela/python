name1 = input('Player 1 what is your name: ')
name2 = input('Player 2 what is your name: ')
while True:
    player1 = input((name1) + ", please choose Rock, Paper or Scissors (r/p/s): ")
    player2 = input((name2) + ", please choose Rock, Paper or Scissors (r/p/s): ")
    if player1 == 'r' and player2 == 's' or player1 == 's' and player2 == 'p' or player1 == 'p' and player2 == 'r':
        print("congratulations to the winner "+name1)
    elif player2 == 'r' and player1 == 's' or player2 == 's' and player1 == 'p' or player2 == 'p' and player1 == 'r':
        print("congratulations to the winner "+name2)
    elif player2 == 'r' and player1 == 'r' or player2 == 'p' and player1 == 'p' or player2 == 's' and player1 == 's':
        print('Draw')
    else:
        print("you have picked a wrong choice")
    playgame=input("want to play new game?say(Y/N)")
    if playgame!="Y":
        break
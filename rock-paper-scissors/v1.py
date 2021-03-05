print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("***NO CHEATING!***\n\n" * 20)
player2 = input("Player 2, make your move: ")

if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player1 wins!")
    elif player2 == "paper":
        print("Player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player1 wins!")
    elif player2 == "scissors":
        print("Player2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player1 wins!")
    elif player2 == "rock":
        print("Player2 wins!")
else:
    print("Something went wrong")
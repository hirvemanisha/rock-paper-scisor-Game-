player=input("what you pick")
computer=input("what you pick")
if player==computer:
        print ('Draw!')
elif player=='rock' and computer == 'scissors':
    print("win")
elif player== 'paper' and computer == 'scissors':
    print("lose")
elif player== 'scissors' and computer == 'paper':
    print("win")
elif player == 'scissors' and computer == 'rock':
    print("lose")
elif player == 'paper' and computer == 'rock':
    print("win")
elif player== 'rock' and computer  == 'paper':
    print("lose")

again = input('Do you want to play again? (y or n)')
if again == "y":
    print("start game again")
elif again=="n":
    print("thank you")
import random

choices = ["Rock", "Paper", "Scissors"]

cpu_score = 0
player_score = 0

Computer = random.choice(choices)
Player = input("Enter YOUR Choice (Rock/Paper/Scissors): ").capitalize()

if Player not in choices:
    print("ERROR: Invalid choice!")
else:
    print(f"Computer chose: {Computer}")
    
    if Player == Computer:
        print("DRAW")
    
    elif (Player == "Paper" and Computer == "Rock") or \
         (Player == "Scissors" and Computer == "Paper") or \
         (Player == "Rock" and Computer == "Scissors"):
        print(f"Player WINS! {Player} beats {Computer}")
        player_score += 1  # fixed
    
    else:
        print(f"Computer WINS! {Computer} beats {Player}")
        cpu_score += 1     # fixed

# Print final scores
print(f"Player score: {player_score} | CPU score: {cpu_score}")

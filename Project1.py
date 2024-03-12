print("Welcome to 1v1 battle\n")
choice = ""
player1Health = 1000
player2Health = 1000

player1 = input("Player 1: Enter your name: ")
player2 = input("Player 2: Enter your name: ")

while choice.lower() != "no":

  damageToPlayer2 = int(input("Player 1: How much damage to player 2: "))

  player2Health -= damageToPlayer2

  damageToPlayer1 = int(input("Player 2: How much damage to player 1: "))

  player1Health -= damageToPlayer1

  choice = input("Would you like to play again? ")


totalDamageToPlayer1 = 1000 - player1Health
totalDamageToPlayer2 = 1000 - player2Health

print(f"In total, {player1} did {totalDamageToPlayer2} to {player2}")
print(f"In total, {player2} did {totalDamageToPlayer1} to {player1}")

if totalDamageToPlayer1 > totalDamageToPlayer2:
  print(f"{player1} wins!")

elif totalDamageToPlayer2 > totalDamageToPlayer1:
  print(f"{player2} wins!")

else:
  print("draw")

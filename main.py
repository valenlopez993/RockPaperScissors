# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

print("\n=========================================================")
print("========== Player 1 is always the bot I built ===========")
print("=========================================================")

print("\n================== Game against quincy ==================\n")
play(player, quincy, 1000)
print("\n================== Game against abbey ===================\n")
play(player, abbey, 1000)
print("\n================== Game against kris ====================\n")
play(player, kris, 1000)
print("\n================= Game against mrugesh ==================\n")
play(player, mrugesh, 1000)
print("\n=========================================================\n")

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)

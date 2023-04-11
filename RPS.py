import random

def player(prev_play, opponent_history=[], playerDetected=["" , False]):
    opponent_history.append(prev_play)

    # Quincy strategy #
    QuincyChoices = ["R", "R", "P", "P", "S"]
    if (not playerDetected[1]) and (len(opponent_history) > 5):
        diff = [ord(q0) - ord(qn) for q0, qn in zip(QuincyChoices, opponent_history[-5:-1])]
        if (sum(diff) == 0):
            playerDetected[1] = True
            playerDetected[0] = "quincy"


    if (playerDetected[1]):
        if (playerDetected[0] == "quincy"): guess = QuincyChoices[(len(opponent_history)+2) % len(QuincyChoices)]
    else:
        guess = random.choice(["R", "P", "S"])

    return guess

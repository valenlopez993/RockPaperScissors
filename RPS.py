import random
import numpy as np

def player(prev_play, opponent_history=[], scoreTable=np.zeros((3, 3, 3))):
    opponent_history.append(prev_play)
    
    #
    #                     / S
    #                    / P
    #                   / R
    #       R   P   S  / 
    #   R |   |   |   |
    #   P |   |   |   |
    #   S |   |   |   |
    #
    
    responses = {'P': 'S', 'R': 'P', 'S': 'R'}
    choices = ['R', 'P', 'S']

    if len(opponent_history) < 4 : 
        guess = random.choice([0, 1, 2])
    else:
        lastPlays = [choices.index(opponent_history[-3]), choices.index(opponent_history[-2]), choices.index(opponent_history[-1])]
        scoreTable[lastPlays[0], lastPlays[1], lastPlays[2]] += 1
        guess = np.argmax(scoreTable[lastPlays[1], lastPlays[2], :])

    return responses[choices[guess]]

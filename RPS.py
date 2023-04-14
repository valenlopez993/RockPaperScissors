import random
import numpy as np

def player(prev_play, opponent_history=[], guessing_history=[], scoreTable=np.zeros((3, 3, 3))):
    if prev_play == '':
        opponent_history.clear()
    else:
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
    remember = 15
    reward = 0
    penalty = 0

    responses = {'P': 'S', 'R': 'P', 'S': 'R'}
    choices = ['R', 'P', 'S']

    if len(opponent_history) < 4 : 
        guess = random.choice(choices)
        guessing_history.append(guess)
        return guess

    lastPlays = [   choices.index(opponent_history[-3]), 
                    choices.index(opponent_history[-2]), 
                    choices.index(opponent_history[-1])]

    m = len(lastPlays)
    back = 0
    while((m < remember) and (m < len(opponent_history))):
        m += 1
        back += 1
        lastPlays.insert(0,choices.index(opponent_history[-m]))

        if guessing_history[-back] == opponent_history[-back]:
            scoreTable[lastPlays[0], lastPlays[1], lastPlays[2]] += reward
        else:
            scoreTable[lastPlays[0], lastPlays[1], lastPlays[2]] += penalty
    
    scoreTable[lastPlays[-3], lastPlays[-2], lastPlays[-1]] += 1

    guess = choices[np.argmax(scoreTable[lastPlays[-2], lastPlays[-1], :])]
    guessing_history.append(guess)
    return responses[guess]

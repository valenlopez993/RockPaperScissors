import random
import numpy as np

def player(prev_play, opponent_history=[], scoreTable=np.zeros((3, 3, 3, 3))):
    if prev_play == '':
        opponent_history.clear()
        scoreTable[:, :, :, :] = 0
    else:
        opponent_history.append(prev_play)

    responses = {'P': 'S', 'R': 'P', 'S': 'R'}
    choices = ['R', 'P', 'S']

    remember = len(scoreTable.shape)   # How far back in time goes the recall 

    if len(opponent_history) < remember : 
        guess = 'P'
        return responses[guess]

    lastPlays = []
    for back in range(1, remember+1):
        lastPlays.insert(0,choices.index(opponent_history[-back]))
    
    scoreTable[lastPlays[-4], lastPlays[-3], lastPlays[-2], lastPlays[-1]] += 1

    guess = choices[np.argmax(scoreTable[lastPlays[-3], lastPlays[-2], lastPlays[-1], :])]
    return responses[guess]

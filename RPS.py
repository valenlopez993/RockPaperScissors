import random
import numpy as np

def player(prev_play, opponent_history=[], guessing_history=[], scoreTable=np.zeros((3, 3, 3, 3, 3, 3)), intertions=[False, 0]):
    if prev_play == '':
        opponent_history.clear()
    else:
        opponent_history.append(prev_play)

    responses = {'P': 'S', 'R': 'P', 'S': 'R'}
    choices = ['R', 'P', 'S']

    remember = len(scoreTable.shape)   # How far back in time goes the recall 

    if len(opponent_history) < remember : 
        guess = random.choice(choices)
        guessing_history.append(guess)
        return guess

    lastPlays = []
    for back in range(1, remember+1):
        lastPlays.insert(0,choices.index(opponent_history[-back]))
    
    

    if len(opponent_history) % 200 == 0: intertions[0] = True
    
    if intertions[0] and intertions[1] < 50:
        intertions[1] += 1
        guess = random.choice(choices)
    else: 
        intertions[1] = 0
        intertions[0] = False

        scoreTable[lastPlays[-6], lastPlays[-5], lastPlays[-4], lastPlays[-3], lastPlays[-2], lastPlays[-1]] += 1

        guess = choices[np.argmax(scoreTable[lastPlays[-5], lastPlays[-4], lastPlays[-3], lastPlays[-2], lastPlays[-1], :])]
    
    guessing_history.append(guess)
    return responses[guess]

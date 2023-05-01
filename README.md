# Rock Paper Scissors

This project was part of the [Free Code Camp Machine Learning course](https://www.freecodecamp.org/learn/machine-learning-with-python/#how-neural-networks-work). The goal of this project was to develop an intelligent algorithm capable of adapting its game to beat different strategies in the classic game Rock, Paper, and Scissors. The project utilized four pre-existing strategies, or bots, which were named:

- Quincy
- Abbey
- Kris
- Mrugesh

To beat these bots, I proposed a strategy that involves creating a NumPy matrix with four dimensions with 3 elements in each dimension. Each dimension represents the opponent's last four plays, and each element inside represents the three possible games: Rock, Paper, or Scissors.

The matrix keeps track of the frequency of each four sequence plays and increments the count of the respective sequence by one after each play. This approach enabled the algorithm to predict the most probable next move of the opponent based on the frequency of past moves. This strategy is coded in the [RPS.py](./RPS.py) file.

The algorithm achieved a minimum of 60% success rate against each bot, which, while not optimal, is still good enough considering the simplicity of the approach.

## [Run the project on Replit](https://replit.com/@ValentinLopez/boilerplate-rock-paper-scissors) 

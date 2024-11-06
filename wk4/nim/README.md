# Nim AI

### Overview
The Nim project implements an AI for the game Nim using Q-learning. By training against itself through reinforcement learning, the AI learns optimal strategies for gameplay, improving its performance over time.

In Nim, players alternate turns, removing objects from a chosen pile. The player forced to remove the last object loses. The AI learns to play Nim by estimating the rewards for each possible move in every game state.

### Usage
1. Begin the training by running `play.py`.
2. Play against the AI by choosing piles to remove objects from, then the number of objects to remove from that pile.

### Example
```bash
$ python play.py
Playing training game 1
Playing training game 2
...
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

Your Turn
Choose Pile: 0
Choose Count: 1

Piles:
Pile 0: 0
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.

Piles:
Pile 0: 0
Pile 1: 3
Pile 2: 4
Pile 3: 7
...
```
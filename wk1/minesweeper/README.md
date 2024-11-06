# Minesweeper AI

### Overview
The goal of this project is to build an AI that can play Minesweeper by using logical inference to identify safe moves and flag mines based on information from revealed cells. This AI acts as a knowledge-based agent that updates its knowledge base with each move, enabling it to reason and deduce where mines may or may not be located on the Minesweeper board.

### Usage
- Download the project files and install dependencies using pip3 install -r requirements.txt.
- Run python runner.py to launch the graphical interface and either play the game manually or let the AI play.
```bash
$ pip install -r requirements.txt
$ python runner.py
```

### Logic and Inference
The AI leverages propositional logic to infer safe moves or locate mines:
- If the count of mines matches the number of cells in a sentence, all cells are mines.
- If the count is zero, all cells in the sentence are safe.
- The AI can combine sentences (using subset inference) to generate new logical conclusions.

### Note
- You may still trigger a mine when making an AI move. There will be some cases where the AI must guess, because it lacks sufficient information to make a safe move.
- `Runner.py` will print whether the AI is making a move it believes to be safe or whether it is making a random move.
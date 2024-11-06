# Knights and Knaves Puzzle Solver

### Overview
This project provides a Python program that solves "Knights and Knaves" logic puzzles. In these puzzles, each character is either a knight, who always tells the truth, or a knave, who always lies. The goal is to determine, based on their statements, who is a knight and who is a knave.

The program models logical sentences based on the characters' statements. Using propositional logic and model checking, it deduces the characters' true nature in each puzzle, solving puzzles automatically by evaluating logical conditions against defined knowledge bases.

### Puzzles
0. A says "I am both a knight and a knave."
1. A says "We are both knaves." B says nothing.
2. A says "We are the same kind." B says "We are of different kinds."
3. A says either "I am a knight." or "I am a knave.", but you don't know which. B says "A said 'I am a knave'." B says "C is a knave." C says "A is a knight."


### Usage
Run the following command to solve the puzzles.
```bash
$ python puzzle.py
```
The output will indicate whether each character is a knight or a knave for each puzzle.


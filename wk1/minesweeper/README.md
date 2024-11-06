# Minesweeper

### Usage
```bash
$ pip install -r requirements.txt
$ python runner.py
```
- Click a cell to reveal it.
- Right click a cell to mark it as a mine.
- Click AI Move to run the AI.

### Note
- You may still trigger a mine when making an AI move. There will be some cases where the AI must guess, because it lacks sufficient information to make a safe move.
- `Runner.py` will print whether the AI is making a move it believes to be safe or whether it is making a random move.
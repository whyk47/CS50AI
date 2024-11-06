"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
	"""
	Returns player who has the next turn on a board.
	"""
	x, o = 0, 0
	for row in board:
		x += row.count('X')
		o += row.count('O')
	if o < x:
		return O
	else:
		return X
	

def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	moves = []
	for row in range(3):
		for col in range(3):
			if board[row][col] == None:
				moves.append((row, col))
	return moves


def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	if board[action[0]][action[1]] != None:
		raise Exception('Invalid move')
	active_player = player(board)
	new_board = copy.deepcopy(board)
	new_board[action[0]][action[1]] = active_player
	return new_board


def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	for player in [X, O]:
		rows = board
		cols = list(zip(board[0], board[1], board[2]))
		diagonals = [[board[i][i]for i in range(3)], [board[j][j] for j in range (2, -1, -1)]]
		for line in rows + cols + diagonals:
			if all([element == player for element in line]):
				return player
	return None


def terminal(board):
	"""
 	Returns True if game is over, False otherwise.
  	"""
	if winner(board) or all([all([element != None for element in row]) for row in board]):
		return True
	return False


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	if winner(board) == X:
		return 1
	elif winner(board) == O:
		return -1
	else:
		return 0


def minimax(board):
  """
  Returns the optimal action for the current player on the board.
  """
  if terminal(board):
    return None
  for action in actions(board):
    if terminal(result(board, action)):
      return action
  optimal_actions = []
  if player(board) == X:
    optimal_val = max_val(board, -2, 2)
    for action in actions(board):
      if min_val(result(board, action), -2, 2) == optimal_val:
        optimal_actions.append(action)
  else: 
    optimal_val = min_val(board, -2, 2)
    for action in actions(board):
      if max_val(result(board, action), -2, 2) == optimal_val:
        optimal_actions.append(action)
  if len(optimal_actions) == 1:
    return optimal_actions[0]
  else:
    diagonals = [(0, 0), (2, 2), (0, 2), (1, 1), (1, 1), (2, 0)]
    num_diagonals = [diagonals.count(action) for action in optimal_actions]
    return optimal_actions[num_diagonals.index(max(num_diagonals))]
      

"""
Alpha is the best value that the maximizer currently can guarantee at that level or above. 
Beta is the best value that the minimizer currently can guarantee at that level or below.
"""

def max_val(board, alpha, beta):
  v = -2
  if terminal(board):
    return utility(board)
  for action in actions(board):
    v = max(v, min_val(result(board, action), alpha, beta))
    alpha = max(v, alpha)
    if beta <= alpha:
      break
  return v


def min_val(board, alpha, beta):
  v = 2
  if terminal(board):
    return utility(board)
  for action in actions(board):
    v = min(v, max_val(result(board, action), alpha, beta))
    beta = min(v, beta)
    if beta <= alpha:
      break
  return v

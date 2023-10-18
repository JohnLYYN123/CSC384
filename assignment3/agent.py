"""
An AI agent for land bidding process.
"""

import random
import sys
import time
import math

# You can use the functions in utilities to write your AI
from utilities import find_lines, get_possible_moves, get_score, play_move

# caching optimization:
    # 1. a dictionary
cached_states = {}

def eprint(*args, **kwargs): #you can use this for debugging, as it will print to sterr and not stdout
    print(*args, file=sys.stderr, **kwargs)

# Method to compute utility value of terminal state
def compute_utility(board, color):
    #IMPLEMENT
    # Some comments:
    # 1. first company = 1 = dark | second company = 2 = light
    # 2. 0 = empty land
    # 3. this function returns the utility of the terminal state

    if color == 1:
        util = get_score(board)[0] - get_score(board)[1]
    else:
        util = get_score(board)[1] - get_score(board)[0]
    return util #change this!

# Better heuristic value of board
def board_corner_check(board, dimension, color):
    # returns the corner score of a color
    score = 0
    if board[0][dimension - 1] == color:
        score = score + 1
    if board[0][0] == color:
        score = score + 1
    if board[dimension - 1][0] == color:
        score = score + 1
    if board[dimension - 1][dimension - 1] == color:
        score = score + 1
    return score

def compute_heuristic(board, color): #not implemented, optional
    #IMPLEMENT
    h_util = 0
    dimension = len(board)

    color2 = other_color(color)
    ally = board_corner_check(board, dimension, color)
    enemy = board_corner_check(board, dimension, color2)

    # check if corners are occupied by any side
    if ally + enemy != 0 and abs(ally - enemy) != 0:
        h_util = 100 * (ally + enemy) / (ally - enemy)
        # h_util = ally - enemy
    else:
        if color == 1:
            h_util = get_score(board)[0] - get_score(board)[1]
        else:
            h_util = get_score(board)[1] - get_score(board)[0]

    return h_util

def other_color(color):
    color2 = 0
    if color == 1:
        color2 = 2
    else:
        color2 = 1
    return color2


def get_util(order):
    return order[0]

############ MINIMAX ###############################
def mm_min_node(board, color, limit, caching = 0):
    #IMPLEMENT (and replace the line below)

    # 1. the opponent is playing select the worst option/utility for us
    # 2. used for the competitor -- minimize our benefits
    # assuming it is the opponent's turn to take the land
    # eprint("the dimension of board", len(board))

    if limit == 0:
        return None, compute_utility(board, color)
        # return None, compute_heuristic(board, color)

    color2 = other_color(color)
    fin_val = math.inf
    moves = get_possible_moves(board, color2)

    # when reaching the terminal state, no other moves can be played
    if len(moves) == 0:
        fin_val = compute_utility(board, color)
        fin_coord = None
        return fin_coord, fin_val

    for i in moves:
        board2 = play_move(board, color2, i[0], i[1])
        # temp_coord, temp_val = mm_max_node(board2, color, limit, caching)
        if limit != 0:
            limit = limit - 1

        if caching == 1:
            if (board2, color2) in cached_states:
                return cached_states.get((board2, color2))

        temp_val = (mm_max_node(board2, color, limit, caching))[1]

        if temp_val < fin_val:
            fin_val = temp_val
            fin_coord = i
            if caching == 1:
                cached_states[(board2, color2)] = (fin_coord, fin_val)
    if caching == 1:
        cached_states[(board2, color2)] = (fin_coord, fin_val)
    return fin_coord, fin_val


def mm_max_node(board, color, limit, caching = 0):
    #IMPLEMENT (and replace the line below)

    # 1. Used for our company
    if limit == 0:
        return None, compute_utility(board, color)
        # return None, compute_heuristic(board, color)

    fin_val = -math.inf
    moves = get_possible_moves(board, color)

    if len(moves) == 0:
        fin_val = compute_utility(board, color)
        fin_coord = None
        return fin_coord, fin_val

    for i in moves:
        board2 = play_move(board, color, i[0], i[1])

        if limit != 0:
            limit = limit - 1

        if caching == 1:
            if (board2, color) in cached_states:
                # print(cached_states.get('(board2, color)'))
                return cached_states.get((board2, color))

        temp_val = mm_min_node(board2, color, limit, caching)[1]

        if temp_val > fin_val:
            fin_val = temp_val
            fin_coord = i

            if caching == 1:
                cached_states[(board2, color)] = (fin_coord, fin_val)

    if caching == 1:
        cached_states[(board2, color)] = (fin_coord, fin_val)
    return fin_coord, fin_val


def claim_mm(board, color, limit, caching = 0):
    """
    Given a board and a player color, decide on a move.
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.

    Note that other parameters are accepted by this function:
    If limit is a positive integer, your code should enfoce a depth limit that is equal to the value of the parameter.
    Search only to nodes at a depth-limit equal to the limit.  If nodes at this level are non-terminal return a heuristic
    value (see compute_utility)
    If caching is ON (i.e. 1), use state caching to reduce the number of state evaluations.
    If caching is OFF (i.e. 0), do NOT use state caching to reduce the number of state evaluations.
    """
    #IMPLEMENT (and replace the line below)
    cached_states.clear()
    fin_coord, fin_val = mm_max_node(board, color, limit, caching)
    return fin_coord #change this!

############ ALPHA-BETA PRUNING #####################
def ab_min_node(board, color, alpha, beta, limit, caching = 0, ordering = 0):
    #IMPLEMENT (and replace the line below)
    # opponent's turn

    if limit == 0:
        return None, compute_utility(board, color)
        # return None, compute_heuristic(board, color)

    color2 = other_color(color)
    moves = get_possible_moves(board, color2)
    fin_val = math.inf
    child_order = []


    if len(moves) == 0:
        fin_val = compute_utility(board, color)
        fin_coord = None
        return fin_coord, fin_val

    if ordering == 1:
        for i in moves:
            board2 = play_move(board, color2, i[0], i[1])
            child_order.append((compute_utility(board2, color), i))
        child_order.sort(key=get_util)

        temp_moves = []

        for j in child_order:
            temp_moves.append(j[1])
        moves = temp_moves


    for i in moves:
        board2 = play_move(board, color2, i[0], i[1])

        if caching == 1:
            if (board2, color) in cached_states:
                # if cached_states.get((board2, color2))[0] != i:
                return cached_states.get((board2, color))

        if limit != 0:
            limit = limit - 1

        temp_val = (ab_max_node(board2, color, alpha, beta, limit, caching, ordering))[1]

        beta = min(beta, temp_val)
        if temp_val < fin_val:
            fin_val = temp_val
            fin_coord = i

            if caching == 1:
                cached_states[(board2, color2)] = (fin_coord, fin_val)

            if alpha >= fin_val:
                if caching == 1:
                    cached_states[(board2, color2)] = (fin_coord, fin_val)
                return fin_coord, fin_val
    if caching == 1:
        cached_states[(board2, color2)] = (fin_coord, fin_val)
    return fin_coord, beta

def ab_max_node(board, color, alpha, beta, limit, caching = 0, ordering = 0):
    #IMPLEMENT (and replace the line below)

    if limit == 0:
        return None, compute_utility(board, color)
        # return None, compute_heuristic(board, color)

    # our turn
    moves = get_possible_moves(board, color)
    fin_val = -math.inf
    child_order = []

    if len(moves) == 0:
        fin_val = compute_utility(board, color)
        fin_coord = None
        return fin_coord, fin_val

    if ordering == 1:
        for i in moves:
            board2 = play_move(board, color, i[0], i[1])
            child_order.append((compute_utility(board2, color), i))
        child_order.sort(key=get_util, reverse=True)

        temp_moves = []

        for j in child_order:
            temp_moves.append(j[1])
        moves = temp_moves

    for i in moves:
        board2 = play_move(board, color, i[0], i[1])

        if caching == 1:
            if (board2, color) in cached_states:
                return cached_states.get((board2, color))

        if limit != 0:
            limit = limit - 1

        temp_val = (ab_min_node(board2, color, alpha, beta, limit, caching, ordering))[1]
        alpha = max(alpha, temp_val)

        if temp_val > fin_val:
            fin_val = temp_val
            fin_coord = i
            if caching == 1:
                cached_states[(board2, color)] = (fin_coord, fin_val)

            if fin_val >= beta:
                if caching == 1:
                    cached_states[(board2, color)] = (fin_coord, fin_val)
                return fin_coord, fin_val

    if caching == 1:
        cached_states[(board2, color)] = (fin_coord, fin_val)
    return fin_coord, alpha

def claim_ab(board, color, limit, caching = 0, ordering = 0):
    """
    Given a board and a player color, decide on a move.
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.

    Note that other parameters are accepted by this function:
    If limit is a positive integer, your code should enfoce a depth limit that is equal to the value of the parameter.
    Search only to nodes at a depth-limit equal to the limit.  If nodes at this level are non-terminal return a heuristic
    value (see compute_utility)
    If caching is ON (i.e. 1), use state caching to reduce the number of state evaluations.
    If caching is OFF (i.e. 0), do NOT use state caching to reduce the number of state evaluations.
    If ordering is ON (i.e. 1), use node ordering to expedite pruning and reduce the number of state evaluations.
    If ordering is OFF (i.e. 0), do NOT use node ordering to expedite pruning and reduce the number of state evaluations.
    """
    #IMPLEMENT (and replace the line below)
    cached_states.clear()
    alpha = -math.inf
    beta = math.inf
    fin_coord, fin_val = ab_max_node(board, color, alpha, beta, limit, caching, ordering)
    return fin_coord #change this!

####################################################
def run_ai():
    """
    This function establishes communication with the game manager.
    It first introduces itself and receives its color.
    Then it repeatedly receives the current score and current board state
    until the game is over.
    """
    print("Bidding AI") # First line is the name of this AI
    arguments = input().split(",")

    color = int(arguments[0]) #Player color: 1 for dark (goes first), 2 for light.
    limit = int(arguments[1]) #Depth limit
    minimax = int(arguments[2]) #Minimax or alpha beta
    caching = int(arguments[3]) #Caching
    ordering = int(arguments[4]) #Node-ordering (for alpha-beta only)

    if (minimax == 1): eprint("Running MINIMAX")
    else: eprint("Running ALPHA-BETA")

    if (caching == 1): eprint("State Caching is ON")
    else: eprint("State Caching is OFF")

    if (ordering == 1): eprint("Node Ordering is ON")
    else: eprint("Node Ordering is OFF")

    if (limit == -1): eprint("Depth Limit is OFF")
    else: eprint("Depth Limit is ", limit)

    if (minimax == 1 and ordering == 1): eprint("Node Ordering should have no impact on Minimax")

    while True: # This is the main loop
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input()
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over.
            print
        else:
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The
                                  # squares in each row are represented by
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)

            # Select the move and send it to the manager
            if (minimax == 1): #run this if the minimax flag is given
                movei, movej = claim_mm(board, color, limit, caching)
            else: #else run alphabeta
                movei, movej = claim_ab(board, color, limit, caching, ordering)

            print("{} {}".format(movei, movej))

if __name__ == "__main__":
    run_ai()

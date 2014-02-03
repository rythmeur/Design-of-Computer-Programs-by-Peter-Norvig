# # -----------------
# # User Instructions
# #
# # Write the two action functions, hold and roll. Each should take a
# # state as input, apply the appropriate action, and return a new
# # state.
# #
# # States are represented as a tuple of (p, me, you, pending) where
# # p:       an int, 0 or 1, indicating which player's turn it is.
# # me:      an int, the player-to-move's current score
# # you:     an int, the other player's current score.
# # pending: an int, the number of points accumulated on current turn, not yet scored
#
# def hold(state):
#     """Apply the hold action to a state to yield a new state:
#     Reap the 'pending' points and it becomes the other player's turn."""
#     # your code here
#
#     #Norvig's brill. => (p, me, you, pending) = state
#
#     new_state = list (state)
#     new_state[0]= ( new_state[0] +1 ) % 2
#     new_state[1],new_state[2] = new_state[2],new_state[1]
#     new_state[2] += new_state[3]
#     new_state[-1] = 0
#     # print tuple(new_state)
#     return tuple(new_state)
#
#
# def roll(state, d):
#     """Apply the roll action to a state (and a die roll d) to yield a new state:
#     If d is 1, get 1 point (losing any accumulated 'pending' points),
#     and it is the other player's turn. If d > 1, add d to 'pending' points."""
#     # your code here
#     if d  == 1:
#         s = list(state)
#         s[-1] = 1
#         state = tuple(s)
#         # print "state", state
#         return hold(state)
#     else:
#         s = list(state)
#         s[-1] += d
#         state = tuple(s)
#         return state
#
# def test():
#     assert hold((1, 10, 20, 7))    == (0, 20, 17, 0)
#     assert hold((0, 5, 15, 10))    == (1, 15, 15, 0)
#     assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
#     assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
#     return 'tests pass'
#
# print test()

# -----------------
# User Instructions
#
# Write a function, play_pig, that takes two strategy functions as input,
# plays a game of pig between the two strategies, and returns the winning
# strategy. Enter your code at line 41.
#
# You may want to borrow from the random module to help generate die rolls.

import random

possible_moves = ['roll', 'hold']
other = {1:0, 0:1}
goal = 50

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def play_pig(A, B):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    # your code here
    strategies = [A,B]
    state = (0,0,0,0)
    while state[1] < goal and state[2] < goal:
        print state
        if strategies[state[0]](state) == "hold":
            state = hold(state)
        else:
            state = roll(state,random.choice([1,2,3,4,5,6]))

    if state[0]==0:
        return B
    else:
        return A



def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

def test():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests pass'

print test()


# # -----------------
# # User Instructions
# #
# # Write a function, bsuccessors(state), that takes a state as input
# # and returns a dictionary of {state:action} pairs.
# #
# # A state is a (here, there, t) tuple, where here and there are
# # frozensets of people (indicated by their times), and potentially
# # the 'light,' t is a number indicating the elapsed time.
# #
# # An action is a tuple (person1, person2, arrow), where arrow is
# # '->' for here to there or '<-' for there to here. When only one
# # person crosses, person2 will be the same as person one, so the
# # action (2, 2, '->') means that the person with a travel time of
# # 2 crossed from here to there alone.
#
# def bsuccessors(state):
#     """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
#     where here and there are frozensets of people (indicated by their times) and/or
#     the 'light', and t is a number indicating the elapsed time. Action is represented
#     as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
#     '<-' for there to here."""
#     here, there, t = state
#     # your code here
#     result = {}
#     if 'light' in here:
#         for chel in here:
#             if chel!= 'light':
#                 result[(here  - frozenset([chel, 'light']),
#                       there | frozenset([chel, 'light']), t+chel)]=  (chel, chel, '->')
#         for chel1 in here:
#             for chel2 in here:
#                 if chel1!= 'light' and chel2!='light' and chel1!=chel2:
#                     result[(here  - frozenset([chel1, chel2, 'light']),
#                           there | frozenset([chel1, chel2, 'light']), t+max(chel1, chel2))]=  (chel1, chel2, '->')
#
#     if 'light' in there:
#         for chel in there:
#             if chel!= 'light':
#                 result[(here | frozenset([chel, 'light']),there  - frozenset([chel, 'light']),
#                        t+chel)]=  (chel, chel, '<-')
#         for chel1 in there:
#             for chel2 in there:
#                 if chel1!= 'light' and chel2!='light' and chel1!=chel2:
#                     result[(here | frozenset([chel1, chel2, 'light']),there  - frozenset([chel1, chel2, 'light']),
#                            t+max(chel1, chel2))]=  (chel1, chel2, '->')
#
#
#
#     return result
#
#
#
#
# def test():
#
#     assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
#                 (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}
#
#     assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
#                 (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
#
#     return 'tests pass'
#
# print  test()

# # ----------------
# # User Instructions
# #
# # Write two functions, path_states and path_actions. Each of these
# # functions should take a path as input. Remember that a path is a
# # list of [state, action, state, action, ... ]
# #
# # path_states should return a list of the states. in a path, and
# # path_actions should return a list of the actions.
#
# def path_states(path):
#     "Return a list of states in this path."
#     return [path[i] for i in range(0,len(path),2)] # Norvig = path[0::2]
#
# def path_actions(path):
#     "Return a list of actions in this path."
#     return  [path[i] for i in range(1,len(path),2)] # Norvig = path[1::2]
#
# def test():
#     testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
#                 (5, 2, '->'),                                        # action 1
#                 (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
#                 (2, 1, '->'),                                        # action 2
#                 (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
#                 (5, 5, '->'),
#                 (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
#                 (5, 10, '->'),
#                 (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
#                 (2, 2, '->'),
#                 (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
#                 (10, 1, '->'),
#                 (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
#                 (10, 10, '->'),
#                 (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
#                 (10, 2, '->'),
#                 (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
#                 (5, 1, '->'),
#                 (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
#                 (1, 1, '->')]
#     assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
#                 (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
#                 (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
#                 (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
#                 (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
#                 (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
#                 (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
#                 (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
#                 (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
#                 (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
#     assert path_actions(testpath) == [(5, 2, '->'), # action 1
#                                       (2, 1, '->'), # action 2
#                                       (5, 5, '->'),
#                                       (5, 10, '->'),
#                                       (2, 2, '->'),
#                                       (10, 1, '->'),
#                                       (10, 10, '->'),
#                                       (10, 2, '->'),
#                                       (5, 1, '->'),
#                                       (1, 1, '->')]
#     return 'tests pass'
#
# print test()

# -----------------
# User Instructions
#
# Modify the bridge_problem(here) function so that it
# tests for goal later: after pulling a state off the
# frontier, not when we are about to put it on the
# frontier.

# def bsuccessors(state):
#     """Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
#     where here and there are frozensets of people (indicated by their times) and/or
#     the light, and t is a number indicating the elapsed time."""
#     here, there, t = state
#     if 'light' in here:
#         return dict(((here  - frozenset([a,b, 'light']),
#                       there | frozenset([a, b, 'light']),
#                       t + max(a, b)),
#                      (a, b, '->'))
#                     for a in here if a is not 'light'
#                     for b in here if b is not 'light')
#     else:
#         return dict(((here  | frozenset([a,b, 'light']),
#                       there - frozenset([a, b, 'light']),
#                       t + max(a, b)),
#                      (a, b, '<-'))
#                     for a in there if a is not 'light'
#                     for b in there if b is not 'light')
#
# def elapsed_time(path):
#     return path[-1][2]
#
# def bridge_problem(here):
#     """Modify this to test for goal later: after pulling a state off frontier,
#     not when we are about to put it on the frontier."""
#     ## modify code below
#     here = frozenset(here) | frozenset(['light'])
#     explored = set() # set of states we have visited
#     # State will be a (people-here, people-there, time-elapsed)
#     frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
#     if not here:
#         return frontier[0]
#     result = []
#     while frontier:
#         path = frontier.pop(0)
#         # print path
#         here1, there1, t1 = state1 = path[-1]
#         if not here1 or here1 == set(['light']):
#             return path
#
#         for (state, action) in bsuccessors(state1).items():
#             if state not in explored:
#                 here, there, t = state
#                 explored.add(state)
#                 path2 = path + [action,  state]
#                 frontier.append(path2)
#                 frontier.sort(key=elapsed_time)
#     return []
# def test():
#     assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2 # the [-1][-1] grabs the total elapsed time
#     assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17
#     return 'tests pass'
#
# print bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1]
# print  [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(0)]

# -----------------
# User Instructions
#
# Write a function, csuccessors, that takes a state (as defined below)
# as input and returns a dictionary of {state:action} pairs.
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings:
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C'
# where 'MM->' means two missionaries travel to the right side.
#
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    actions_to_there = {'MM->':[2,0], 'MC->':[1,1], 'CC->':[0,2], 'M->':[1,0], 'C->':[0,1]}
    actions_from_there ={'<-MM':[2,0], '<-MC':[1,1],'<-CC':[0,2], '<-M':[1,0], '<-C':[0,1]}
    # your code here
    result ={}
    if M1<C1 or M2<C2: return {}
    if B1 !=0:
        # z = [(M1-m, C1-c) for m in range(M1+1) for c in range (C1+1) if (m +c <=3)]
        for a in actions_to_there:
            result[(M1-actions_to_there[a][0], C1-actions_to_there[a][1],0,M2+actions_to_there[a][0], C2+actions_to_there[a][1],1 )] = a
    if B2 !=0:
        for a in actions_from_there:
            result[(M1+actions_from_there[a][0], C1+actions_from_there[a][1],1,M2-actions_from_there[a][0], C2-actions_from_there[a][1],0 )] = a


    return result





def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print test()




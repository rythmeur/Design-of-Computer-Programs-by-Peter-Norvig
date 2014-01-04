# # This Python file uses the following encoding: utf-8
#
# def sq(x): print "sq called", x; y = 454;  return x * x #можно в одну строку, разделяя ;
#
# for _ in range(2): #interesting
#     print _
#
# # ----------------
# # User Instructions
# #
# # Modify the timedcalls(n, fn, *args) function so that it calls
# # fn(*args) repeatedly. It should call fn n times if n is an integer
# # and up to n seconds if n is a floating point number.
#
# import itertools
#
# def imright(h1, h2):
#     "House h1 is immediately right of h2 if h1-h2 == 1."
#     return h1-h2 == 1
#
# def nextto(h1, h2):
#     "Two houses are next to each other if they differ by 1."
#     return abs(h1-h2) == 1
#
# def zebra_puzzle():
#     "Return a tuple (WATER, ZEBRA indicating their house numbers."
#     houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
#     orderings = list(itertools.permutations(houses)) # 1
#     return next((WATER, ZEBRA)
#                 for (red, green, ivory, yellow, blue) in orderings
#                 if imright(green, ivory)
#                 for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
#                 if Englishman is red
#                 if Norwegian is first
#                 if nextto(Norwegian, blue)
#                 for (coffee, tea, milk, oj, WATER) in orderings
#                 if coffee is green
#                 if Ukranian is tea
#                 if milk is middle
#                 for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
#                 if Kools is yellow
#                 if LuckyStrike is oj
#                 if Japanese is Parliaments
#                 for (dog, snails, fox, horse, ZEBRA) in orderings
#                 if Spaniard is dog
#                 if OldGold is snails
#                 if nextto(Chesterfields, fox)
#                 if nextto(Kools, horse)
#                 )
#
# import time
#
# def timedcall(fn, *args):
#     "Call function with args; return the time in seconds and result."
#     t0 = time.clock()
#     result = fn(*args)
#     t1 = time.clock()
#     return t1-t0, result
#
# def average(numbers):
#     "Return the average (arithmetic mean) of a sequence of numbers."
#     return sum(numbers) / float(len(numbers))
#
# def timedcalls(n, fn, *args):
#     """Call fn(*args) repeatedly: n times if n is an int, or up to
#     n seconds if n is a float; return the min, avg, and max time"""
#     # Your code here.
#     if isinstance(n, int):
#         times = [timedcall (fn, *args)[0]  for _ in range (n)]
#
#     else:
#         times = []
#         while sum(times) < n:
#             times.append(timedcall (fn, *args)[0])
#     return min(times), average(times), max(times)
#
# print timedcalls (100, zebra_puzzle)


# User Instructions
#
# Define a function, all_ints(), that generates the
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    j = ints(0)

    while True:
        return (b * z
            for b in j
            for z in [1, -1]
            if (b*z != 0 or z == -1))
    # #another solution
    # yield 0
    # for i in ints(1):
    #     yield +i
    #     yield -i

v = all_ints()
for zz in range (10):
    print next(v)
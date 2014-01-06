#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def higher(f2, f1):
    "Floor f2 is higher than f1"
    return f2-f1 > 0

def adjacent(f1, f2):
    "Two floors are next to each other if they differ by 1."
    return abs(f1-f2) == 1

def floor_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    floors = first, second, third, forth, fifth = [1, 2, 3, 4, 5]  # interesting!
    orderings = list(itertools.permutations(floors)) # 1
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in c(orderings)
                if Hopper != fifth
                if Kay != first
                if Liskov != fifth and Liskov != first
                if higher(Perlis,Kay)
                if not adjacent(Ritchie,Liskov)
                if not adjacent(Liskov,Kay)
    )

def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item
c.starts, c.items = 0, 0
def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items'%(
        fn.__name__, result, c.starts, c.items))

# print instrument_fn(floor_puzzle)
print floor_puzzle()

print  [a for a in [1, 2] ]
houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
print houses
print first

import itertools
floors = first, _, middle, _, _ = [1, 2, 3, 4, 5]  # interesting!
orderings = list(itertools.permutations(floors))
for (red, green, ivory, yellow, blue) in orderings:
    print (red, green, ivory, yellow, blue)
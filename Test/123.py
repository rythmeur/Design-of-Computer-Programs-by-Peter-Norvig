# print  [a for a in [1, 2] ]
# houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
# print houses
# print first
#
# import itertools
# floors = first, _, middle, _, _ = [1, 2, 3, 4, 5]  # interesting!
# orderings = list(itertools.permutations(floors))
# for (red, green, ivory, yellow, blue) in orderings:
#     print (red, green, ivory, yellow, blue)

# x  = set([1, 2, 3])
# z = sum(x)
# print z
#
# print set('theseletters')
#
# z= "a b c d t f ew dsd fda"
# x = z.split(" ", 2)
# print x
#
# z,zz = ["aa", "bb"]
# print z, zz
#
# z= [0, 1, 2]
# print z
# z.reverse()
# print z

# import re
# text = "Though I"
# # text = "<         b           > this <   /b    >, Though I"
# match_i = re.search("(<)(?: *)(.)",text)
# print type(match_i)
# if match_i:
#     print "Nontype"
# # match_i = match_i.groups()
# print match_i
#
#
# a = (1,4,6)
# p = (2,5,8)
# print a <= p
#
# x= list((1,2,5,8))
# print x
# z= tuple(x)
# print z
#
# a={}
# a[1] = 20
#
# a.update({2:15})
# a[2]={3:18}
# a[2].update({4:28})
# a[2]={3:49}
# print a

# def my_function():
#     try:
#         1 / 0
#     except ZeroDivisionError:
#         print "pass"
#
# if __name__ == "__main__":
#     import timeit
#     setup = "from __main__ import my_function"
#     print timeit.timeit("my_function()", setup=setup)



from itertools import *
perm = permutations('ABCDFER', 2)
comb = combinations('ABCD', 3)
comb_with_repl = combinations_with_replacement('ABC', 2)

print "permutations: ",
for n,i in enumerate(perm):
    print i,
print n+1
print "combinations: ",
for n,i in enumerate (comb):
    print i,
print n+1
print "combinations_with_replacement: ",
for n,i in enumerate(comb_with_repl):
    print i,
print n+1

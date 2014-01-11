# #---------------
# # User Instructions
# #
# # Fill out the API by completing the entries for alt,
# # star, plus, and eol.
#
#
# def lit(string):  return ('lit', string)
# def seq(x, y):    return ('seq', x, y)
# def alt(x, y):    return ('alt',x, y)# ??
# def star(x):      return ('star', x)# ??
# def plus(x):      return  ('seq', x, star(x))# ??
# def opt(x):       return alt(lit(''), x) #opt(x) means that x is optional
# def oneof(chars): return ('oneof', tuple(chars))
# dot = ('dot',)
# eol = "" #??
#
# def test():
#     assert lit('abc')         == ('lit', 'abc')
#     assert seq(('lit', 'a'),
#                ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))
#     assert alt(('lit', 'a'),
#                ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))
#     assert star(('lit', 'a')) == ('star', ('lit', 'a'))
#     assert plus(('lit', 'c')) == ('seq', ('lit', 'c'),
#                                   ('star', ('lit', 'c')))
#     assert opt(('lit', 'x'))  == ('alt', ('lit', ''), ('lit', 'x'))
#     assert oneof('abc')       == ('oneof', ('a', 'b', 'c'))
#     return 'tests pass'

# #---------------
# # User Instructions
# #
# # Complete the search and match functions. Match should
# # match a pattern only at the start of the text. Search
# # should match anywhere in the text.
#
# def search(pattern, text):
#     "Match pattern anywhere in text; return longest earliest match or None."
#     for i in range(len(text)):
#         m = match(pattern, text[i:])
#         if m:# your code here
#             return m
#
# def match(pattern, text):
#     "Match pattern against start of text; return longest match found or None."
#     remainders = matchset(pattern, text)
#     if remainders:
#         shortest = min(remainders, key=len)
#         return text[:len(text) - len(shortest)] # your code here
#
# def components(pattern):
#     "Return the op, x, and y arguments; x and y are None if missing."
#     x = pattern[1] if len(pattern) > 1 else None
#     y = pattern[2] if len(pattern) > 2 else None
#     return pattern[0], x, y
#
# def matchset(pattern, text):
#     "Match pattern at start of text; return a set of remainders of text."
#     op, x, y = components(pattern)
#     if 'lit' == op:
#         return set([text[len(x):]]) if text.startswith(x) else null
#     elif 'seq' == op:
#         return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
#     elif 'alt' == op:
#         return matchset(x, text) | matchset(y, text)
#     elif 'dot' == op:
#         return set([text[1:]]) if text else null
#     elif 'oneof' == op:
#         return set([text[1:]]) if text.startswith(x) else null
#     elif 'eol' == op:
#         return set(['']) if text == '' else null
#     elif 'star' == op:
#         return (set([text]) |
#                 set(t2 for t1 in matchset(x, text)
#                     for t2 in matchset(pattern, t1) if t1 != text))
#     else:
#         raise ValueError('unknown pattern: %s' % pattern)
#
# null = frozenset()
#
# def lit(string):  return ('lit', string)
# def seq(x, y):    return ('seq', x, y)
# def alt(x, y):    return ('alt', x, y)
# def star(x):      return ('star', x)
# def plus(x):      return seq(x, star(x))
# def opt(x):       return alt(lit(''), x)
# def oneof(chars): return ('oneof', tuple(chars))
# dot = ('dot',)
# eol = ('eol',)
#
# def test():
#     assert match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
#     assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
#     assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
#     assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
#     return 'tests pass'
#
# print test()

#----------------
# User Instructions
#
# Write the compiler for alt(x, y) in the same way that we
# wrote the compiler for lit(s) and seq(x, y).

'''
def matchset(pattern, text):
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
'''

# def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null
#
# def seq(x, y): return lambda text: set().union(*map(y, x(text)))
#
# def alt(x, y):return lambda text: set().union(x(text) ,y(text)) # your code here
#
# null = frozenset([])
#
# def test():
#     g = alt(lit('a'), lit('b'))
#     print g('abc')
#     # assert g('abc') == set(['bc'])
#     return 'test passes'
#
# print test()

# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars).

# def lit(s):         return lambda Ns: set([s]) if len(s) in Ns else null
# def alt(x, y):      return lambda Ns:  x(Ns)| y(Ns)# your code here
# def star(x):        return lambda Ns: opt(plus(x))(Ns)
# def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky
# def oneof(chars):   return lambda Ns: set([ch for ch in chars]) if (sum (Ns)) == len (set([ch for ch in chars]) ) else null # set('theseletters') - without any loop
# def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
# def opt(x):         return alt(epsilon, x)
# dot = oneof('?')    # You could expand the alphabet to more chars.
# epsilon = lit('')   # The pattern that matches the empty string.
#
# null = frozenset([])
#
# def test():
#
#     f = lit('hello')
#     assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
#     assert f(set([1, 2, 3, 4]))    == null
#
#     g = alt(lit('hi'), lit('bye'))
#     assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
#     assert g(set([1, 3, 5])) == set(['bye'])
#
#     h = oneof('theseletters')
#     assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
#     assert h(set([2, 3, 4])) == null
#
#     return 'tests pass'
#
#
# h = oneof('theseletters')
# print  h(set([1, 2, 3]))
# print test()

# # ---------------
# # User Instructions
# #
# # Write a function, n_ary(f), that takes a binary function (a function
# # that takes 2 inputs) as input and returns an n_ary function.
#
# def n_ary(f):
#     """Given binary function f(x, y), return an n_ary function such
#     that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
#     def n_ary_f(x, *args):
#         # your code here
#         new_args =(x,) + (args)
#         length = len(new_args)
#         result = x
#
#         if length >2:
#             result = f(new_args[length-2], new_args[length-1])
#             for i in range (length-3,-1,-1):
#                 result = f(new_args[i], result)
#
#         return result
#     return n_ary_f
#
# def f(x,q):
#     return x*q
# print n_ary(f)(3,4,5,6,7,8)
# print n_ary(f)(5)

# ---------------
# User Instructions
#
# Modify the function, trace, so that when it is used
# as a decorator it gives a trace as shown in the previous
# video. You can test your function by applying the decorator
# to the provided fibonnaci function.
#
# Note: Running this in the browser's IDE will not display
# the indentations.

from functools import update_wrapper


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(*args)# your code here
            print '%s<-- %s == %s' % ((trace.level-1)*indent,
                                      signature, result)
        finally:
            trace.level -=1 # your code here
        return result# your code here
    trace.level = 0
    return _f

@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(6) #running this in the browser's IDE  will not display the indentations!
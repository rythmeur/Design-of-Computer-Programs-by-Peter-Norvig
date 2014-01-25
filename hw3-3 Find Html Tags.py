# ---------------
# User Instructions
#
# Write a function, findtags(text), that takes a string of text
# as input and returns a list of all the html start tags in the
# text. It may be helpful to use regular expressions to solve
# this problem.

import re
# My very stupid answer
# def findtags(text):
#     # your code here
#     z=text.replace("<","SPLIT_MARGIN<")
#     splited_text = z.split("SPLIT_MARGIN")
#     splited_text2 = splited_text[:]
#     indices_to_del = []
#     for i in range(len(splited_text)):
#         match_i = re.search("(<)(?: *)(.)",splited_text[i])
#         if match_i:
#             match_i = match_i.groups()
#             closing = False
#             if len(match_i)>0:
#                 # print "match_i", match_i, match_i[-1]
#                 for j in range(i+1,len(splited_text)):
#                     if "/" + match_i[-1] in splited_text[j]:
#                         closing = True
#             if not closing:
#                 indices_to_del.append(i)
#     # print "splited_text", splited_text2
#     indices_to_del.reverse()
#     for i in indices_to_del:
#         del splited_text2[i]
#
#     result = []
#     # print "splited_text", splited_text2
#     for string in splited_text2:
#         if "/" not in string:
#             result += re.findall('<.*?>',string)
#     return result

#Peter Norvig answer
def findtags(text):
    parms = '(?:\w+\s*=\s*"[^"]*"\s*)*'
    tags = '(<\s*\w+\s*' + parms + '\s*/?>)'
    return re.findall(tags,text)


testtext1 = """
My favorite website in the world is probably
<a href="www.udacity.com">Udacity</a>. If you want
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you
handle this one. Did you know that 2 < 3 should return True?
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I
don't know why you would ever want to.
"""

def test():
    assert findtags(testtext1) == ['<a href="www.udacity.com">',
                                   '<b>',
                                   '<a href="www.udacity.com"target="_blank">']
    assert findtags(testtext2) == []
    assert findtags(testtext3) == ['<         b           >']
    return 'tests pass'

# print test()
# print findtags(testtext1)
# print findtags(testtext2)
# print findtags(testtext3)

testtext4 = """
<         b           > this </b    >
"""

print findtags(testtext4)

# findtags(testtext1)
# findtags(testtext2)
# findtags(testtext3)
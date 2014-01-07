# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

#http://tarokuriyama.com/projects/palindrome2.php
#http://www.akalin.cx/longest-palindrome-linear-time

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here


def longest_subpalindrome_slice(seq):
    seq = seq.lower()
    # print seq
    if seq == "": return  (0,0)
    """
    Behaves identically to naiveLongestPalindrome (see below), but
    runs in linear time.
    """
    seqLen = len(seq)
    l = []
    i = 0
    palLen = 0
    # Loop invariant: seq[(i - palLen):i] is a palindrome.
    # Loop invariant: len(l) >= 2 * i - palLen. The code path that
    # increments palLen skips the l-filling inner-loop.
    # Loop invariant: len(l) < 2 * i + 1. Any code path that
    # increments i past seqLen - 1 exits the loop early and so skips
    # the l-filling inner loop.
    while i < seqLen:
        # First, see if we can extend the current palindrome.  Note
        # that the center of the palindrome remains fixed.
        if i > palLen and seq[i - palLen - 1] == seq[i]:
            palLen += 2
            i += 1
            continue

        # The current palindrome is as large as it gets, so we append
        # it.
        l.append(palLen)

        # Now to make further progress, we look for a smaller
        # palindrome sharing the right edge with the current
        # palindrome.  If we find one, we can try to expand it and see
        # where that takes us.  At the same time, we can fill the
        # values for l that we neglected during the loop above. We
        # make use of our knowledge of the length of the previous
        # palindrome (palLen) and the fact that the values of l for
        # positions on the right half of the palindrome are closely
        # related to the values of the corresponding positions on the
        # left half of the palindrome.

        # Traverse backwards starting from the second-to-last index up
        # to the edge of the last palindrome.
        s = len(l) - 2
        e = s - palLen
        for j in xrange(s, e, -1):
            # d is the value l[j] must have in order for the
            # palindrome centered there to share the left edge with
            # the last palindrome.  (Drawing it out is helpful to
            # understanding why the - 1 is there.)
            d = j - e - 1

            # We check to see if the palindrome at l[j] shares a left
            # edge with the last palindrome.  If so, the corresponding
            # palindrome on the right half must share the right edge
            # with the last palindrome, and so we have a new value for
            # palLen.
            if l[j] == d: # *
                palLen = d
                # We actually want to go to the beginning of the outer
                # loop, but Python doesn't have loop labels.  Instead,
                # we use an else block corresponding to the inner
                # loop, which gets executed only when the for loop
                # exits normally (i.e., not via break).
                break

            # Otherwise, we just copy the value over to the right
            # side.  We have to bound l[i] because palindromes on the
            # left side could extend past the left edge of the last
            # palindrome, whereas their counterparts won't extend past
            # the right edge.
            l.append(min(d, l[j]))
        else:
            # This code is executed in two cases: when the for loop
            # isn't taken at all (palLen == 0) or the inner loop was
            # unable to find a palindrome sharing the left edge with
            # the last palindrome.  In either case, we're free to
            # consider the palindrome centered at seq[i].
            palLen = 1
            i += 1

    # We know from the loop invariant that len(l) < 2 * seqLen + 1, so
    # we must fill in the remaining values of l.

    # Obviously, the last palindrome we're looking at can't grow any
    # more.
    l.append(palLen)

    # Traverse backwards starting from the second-to-last index up
    # until we get l to size 2 * seqLen + 1. We can deduce from the
    # loop invariants we have enough elements.
    lLen = len(l)
    s = lLen - 2
    e = s - (2 * seqLen + 1 - lLen)
    for i in xrange(s, e, -1):
        # The d here uses the same formula as the d in the inner loop
        # above.  (Computes distance to left edge of the last
        # palindrome.)
        d = i - e - 1
        # We bound l[i] with min for the same reason as in the inner
        # loop above.
        l.append(min(d, l[i]))
    t = [l[i] for i in range(1, len (l),2)]
    max_in_l = max(l)
    position_of_max_element = l.index(max_in_l)/2
    result = (position_of_max_element - (max_in_l / 2) , position_of_max_element + (max_in_l / 2) + (max_in_l % 2) )
    # print l, t, max_in_l, position_of_max_element, result

    return result

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxxx') == (0, 6)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()

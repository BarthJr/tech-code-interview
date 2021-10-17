# A student is taking a cryptography class and has found anagrams to be very useful.
# Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string.
# In other words, both strings must contain the same exact letters in the same exact frequency.
# For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
#
# The student decides on an encryption scheme that involves two large strings.
# The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams.
# Determine this number.
#
# Given two strings, A and B, that may or may not be of the same length,
# determine the minimum number of character deletions required to make A and B anagrams.
# Any characters can be deleted from either of the strings.

"""
>>> makeAnagram('cde', 'dcf')
2
>>> makeAnagram('cde', 'abc')
4
>>> makeAnagram('bacdc', 'dcbac')
0
>>> makeAnagram('bacdc', 'dcbad')
2
>>> makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')
30
"""


def makeAnagram(a, b):
    counter = {}
    incrementCounter(counter, a)
    decrementCounter(counter, b)
    minimumCharsToDelete = sum(abs(value) for value in counter.values())
    return minimumCharsToDelete


def incrementCounter(counter, a):
    for element in a:
        counter[element] = counter.get(element, 0) + 1


def decrementCounter(counter, a):
    for element in a:
        counter[element] = counter.get(element, 0) - 1

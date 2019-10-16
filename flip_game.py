# https://www.lintcode.com/problem/flip-game/description

# You are playing the following Flip Game with your friend: Given a string that contains only these two characters:
# + and -, you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to compute all possible states of the string after one valid move.

"""
>>> Solution().generatePossibleNextMoves('++++')
['--++', '+--+', '++--']
>>> Solution().generatePossibleNextMoves('---+++-+++-+')
['-----+-+++-+', '---+---+++-+', '---+++---+-+', '---+++-+---+']
"""


class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """

    def generatePossibleNextMoves(self, s):
        result = []
        i = 0
        while i + 1 < len(s):
            if s[i] == '+' and s[i + 1] == '+':
                result.append(s[:i] + '-' + '-' + s[i + 2:])
            i += 1

        return result

# You're given three inputs, all of which are instances of a class that have an "ancestor"
# property pointing to their youngest ancestor.
# The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor),
# and the other two inputs are descendants in the ancestral tree.
# Write a function that returns the youngest common ancestor to the two descendants.


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addsAnAncestor(self, descendants):
        for descendant in descendants:
            descendant.ancestor = self


def getYoungestCommonAncestor(topAncestor, descendant_one, descendant_two):
    depth_one = get_descendent_depth(descendant_one)
    depth_two = get_descendent_depth(descendant_two)
    if depth_one > depth_two:
        return backtrack_ancestral(descendant_one, descendant_two, depth_one - depth_two)
    else:
        return backtrack_ancestral(descendant_two, descendant_one, depth_two - depth_one)


def get_descendent_depth(node):
    depth = 0
    while node:
        node = node.ancestor
        depth += 1
    return depth


def backtrack_ancestral(one, two, depth_diff):
    for i in range(depth_diff):
        one = one.ancestor
    while one != two:
        one = one.ancestor
        two = two.ancestor
    return one


ancestralTrees = {}

LETTERS = list('ABCDEFGHI')
for letter in LETTERS:
    ancestralTrees[letter] = AncestralTree(letter)

ancestralTrees['A'].addsAnAncestor([
    ancestralTrees['B'],
    ancestralTrees['C']
])
ancestralTrees['B'].addsAnAncestor([
    ancestralTrees['D'],
    ancestralTrees['E'],
])
ancestralTrees['C'].addsAnAncestor([
    ancestralTrees['F'],
    ancestralTrees['G'],
])
ancestralTrees['D'].addsAnAncestor([
    ancestralTrees['H'],
    ancestralTrees['I'],
])

if __name__ == '__main__':
    result = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['A'], ancestralTrees['B'])
    assert result == ancestralTrees['A']
    result = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['B'], ancestralTrees['F'])
    assert result == ancestralTrees['A']
    result = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['C'], ancestralTrees['G'])
    assert result == ancestralTrees['C']

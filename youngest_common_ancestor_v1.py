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


def getYoungestCommonAncestor(top_ancestor, descendant_one, descendant_two):
    return get_lca(top_ancestor, descendant_one, descendant_two)


def get_lca(ancestor, descendant_one, descendant_two):
    lowest = None
    path_one = path_to_root(descendant_one)
    path_two = path_to_root(descendant_two)

    while path_one and path_two:
        pop_one = path_one.pop()
        pop_two = path_two.pop()
        if pop_one == pop_two:
            lowest = pop_one
        else:
            break

    return lowest


def path_to_root(node):
    path = [node]
    while node:
        node = node.ancestor
        path.append(node)
    return path


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

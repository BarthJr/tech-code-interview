#   You're given a list of arbitrary jobs that need to be completed; these jobs
#   are represented by distinct integers. You're also given a list of dependencies.
#   A dependency is represented as a pair of jobs where the first job is a
#   prerequisite of the second one. In other words, the second job depends on the
#   first one; it can only be completed once the first job is completed.
#
#   Write a function that takes in a list of jobs and a list of dependencies and
#   returns a list containing a valid order in which the given jobs can be
#   completed. If no such order exists, the function should return an empty array.

"""
>>> topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]])
[4, 1, 3, 2]
>>> topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3], [3, 4]])
[]
"""


# O(jobs + deps) time | O(jobs + deps) space
def topologicalSort(jobs, deps):
    graph = JobGraph(jobs, deps)
    return getOrderedJobs(graph)


def getOrderedJobs(graph):
    orderedJobs = []

    while graph.nodes:
        node = graph.nodes.pop()
        hasCycle = dfs(node, orderedJobs)
        if hasCycle:
            return []

    return orderedJobs


def dfs(node, orderedJobs):
    if node.isVisited:
        return False
    if node.isVisiting:
        return True

    node.isVisiting = True

    for preReq in node.preReqs:
        hasCycle = dfs(preReq, orderedJobs)
        if hasCycle:
            return True

    node.isVisited = True
    node.isVisiting = False
    orderedJobs.append(node.value)

    return False


class JobGraph:
    def __init__(self, jobs, deps):
        self.nodes = []
        self.graph = {}

        self.addNodes(jobs)
        self.addPreReqs(deps)

    def addNodes(self, jobs):
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        node = JobNode(job)

        self.nodes.append(node)
        self.graph[job] = node

    def addPreReqs(self, deps):
        for preReq, dep in deps:
            self.addPreReq(preReq, dep)

    def addPreReq(self, preReq, job):
        self.graph[job].preReqs.append(self.graph[preReq])


class JobNode:
    def __init__(self, value):
        self.value = value
        self.preReqs = []
        self.isVisited = self.isVisiting = False

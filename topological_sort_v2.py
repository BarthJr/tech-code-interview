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
    result = []
    noPreReqs = list(filter(lambda node: not node.numOfPreReqs, graph.nodes))

    while noPreReqs:
        job = noPreReqs.pop()
        result.append(job.value)
        removeDeps(job, noPreReqs)
    graphHasEdges = any(node.numOfPreReqs for node in graph.nodes)

    return [] if graphHasEdges else result


def removeDeps(job, result):
    while job.deps:
        node = job.deps.pop()
        node.numOfPreReqs -= 1
        if not node.numOfPreReqs:
            result.append(node)


class JobGraph:
    def __init__(self, jobs, deps):
        self.nodes = []
        self.graph = {}

        self.addNodes(jobs)
        self.addDeps(deps)

    def addNodes(self, jobs):
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        node = JobNode(job)
        self.nodes.append(node)
        self.graph[job] = node

    def addDeps(self, deps):
        for job, dep in deps:
            self.addDep(job, dep)

    def addDep(self, job, dep):
        self.graph[job].deps.append(self.graph[dep])
        self.graph[dep].numOfPreReqs += 1


class JobNode:
    def __init__(self, value):
        self.value = value
        self.deps = []
        self.numOfPreReqs = 0

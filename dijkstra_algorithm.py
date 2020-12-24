# You're given an integer 'start' and a list of 'edges' of pairs of integers.
#
# Write a function that computes the lengths of the shortest paths between 'start'
# and all of the other vertices in the graph using Dijkstra's algorithm and returns them in an array.
# Each index 'i' in the output array should represent the length of the shortest path between 'start' and vertex 'i'.
# If no path is found from 'start' to vertex 'i', then 'output[i]' should be -1.
#
# Note that the graph represented by 'edges' won't contain any
# self-loops (vertices that have an outbound edge to themselves) and will only
# have positively weighted edges (i.e., no negative distances).

"""
>>> dijkstrasAlgorithm(0, [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []])
[0, 7, 13, 27, 10, -1]
"""

import heapq


def dijkstrasAlgorithm(start, edges):
    distances = [float('inf') for _ in range(len(edges))]
    distances[start] = 0
    pq = [(start, 0)]

    while pq:
        currentVertex, currentWeight = heapq.heappop(pq)

        if currentWeight > distances[currentVertex]:
            continue

        neighbors = edges[currentVertex]

        for vertex, weight in neighbors:
            distance = currentWeight + weight
            if distance < distances[vertex]:
                distances[vertex] = distance
                heapq.heappush(pq, (vertex, distance))

    return [distance if distance != float('inf') else -1 for distance in distances]

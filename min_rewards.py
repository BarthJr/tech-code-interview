# Imagine that you're a teacher who's just graded the final exam in a class.
# You have a list of student scores on the final exam in a particular order (not necessarily sorted),
# and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules:
# first, all students must receive at least one reward;
# second, any given student must receive strictly more rewards
# than an adjacent student (a student immediately to the left or to the right)
# with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score.
# Assume that all students have different scores; in other words, the scores are all unique.
# Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out
# to students, all the while satisfying the two rules.

"""
>>> minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5])
25
"""


def minRewards(scores):
    rewards = [1 for _ in scores]

    for i in range(1, len(rewards)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return sum(rewards)

"""
Difficulty: Hard

Given an array of strings words representing an ordered dictionary, return a string representing how the words are
ordered when the words are turned around. You can assume that there are no duplicate words in the dictionary.

For example, given words = ["wrt", "wrf", "er", "ett", "rftt"], return "w->e->r->t->f".
"""

from typing import List
from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # step 0: create data structures + the in_degree of each unique letter to 0
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        # step 1: we need to populate adj_list and in_degree
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
                else:
                    if len(second_word) < len(first_word):
                        return ""

        print(adj_list)
        print(in_degree)

        # step 2: we need to repeatedly pick off nodes with an indegree of 0
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        if len(output) < len(in_degree):
            return ""

        return "->".join(output)


if __name__ == '__main__':
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    solution = Solution()
    print(solution.alienOrder(words))

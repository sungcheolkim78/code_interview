from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break

        return True


if __name__ == '__main__':
    solution = Solution()
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(solution.isAlienSorted(words, order))

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(solution.isAlienSorted(words, order))

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(solution.isAlienSorted(words, order))

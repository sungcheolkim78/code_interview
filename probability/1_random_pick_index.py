import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.map = {}

        for i, num in enumerate(nums):
            self.map[num] = self.map.get(num, []) + [i]

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])


if __name__ == '__main__':
    solution = Solution([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])
    print(solution.pick(3))
    print(solution.pick(6))
    print(solution.pick(1))
    print(solution.pick(2))
    print(solution.pick(5))
    print(solution.pick(6))

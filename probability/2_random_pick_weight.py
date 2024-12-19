from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.cumsum = []
        self.total_sum = 0

        for weight in w:
            self.total_sum += weight
            self.cumsum.append(self.total_sum)

    def pick(self) -> int:
        """
        w = [1, 3, 1]
        index = [0, 1, 1, 1, 2]
        cumsum = [1, 4, 5]
        final_index = [0, 1, 2]
        """

        target = random.randint(1, self.total_sum)

        l, r = 0, len(self.cumsum)
        while l < r:
            mid = l + (r - l) // 2
            if self.cumsum[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l


if __name__ == '__main__':
    solution = Solution([1, 3])
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())

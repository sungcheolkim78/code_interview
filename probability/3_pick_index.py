from typing import List
import random
from collections import Counter


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target <= self.prefix_sums[mid]:
                high = mid
            else:
                low = mid + 1

        return low


if __name__ == '__main__':
    w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = Solution(w)

    output = [solution.pickIndex() for _ in range(1000)]
    output_counter = Counter(output)
    print([output_counter[v] for v in sorted(output_counter.keys())])

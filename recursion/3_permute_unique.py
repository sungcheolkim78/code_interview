from typing import List, Dict
from collections import Counter


def permute_unique(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(combination: List[int], counter: Dict[int, int]):
        if len(combination) == len(nums):
            result.append(list(combination))
            return

        for num in counter:
            if counter[num] > 0:
                combination.append(num)
                counter[num] -= 1

                backtrack(combination, counter)
                combination.pop()
                counter[num] += 1

    backtrack([], Counter(nums))
    return result


if __name__ == '__main__':
    print(permute_unique([1, 2, 3]))
    print(permute_unique([1, 1, 2]))

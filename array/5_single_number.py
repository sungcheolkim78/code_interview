from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return 2 * sum(nums_set) - sum(nums)


if __name__ == '__main__':
    nums = [2, 2, 1, 4, 4, 3, 5, 3, 5]
    solution = Solution()
    print(solution.singleNumber(nums))

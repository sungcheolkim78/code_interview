"""
1, 2, 3, 4
   |, swap
1, 2, 4, 3
   |, swap, swap
1, 3, 2, 4
   |, swap
1, 3, 4, 2
   |, swap, swap
1, 4, 2, 3
   |  swap
1, 4, 3, 2
   |
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first number that is larger than its predecessor
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        # find the last number that is larger than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        print(i, j)

        # reverse the rest of the array
        self.reverse(nums, i + 1)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3]
    print(nums)
    solution.nextPermutation(nums)
    print(nums)

    nums = [1, 2, 3, 4]
    print(nums)
    solution.nextPermutation(nums)
    print(nums)

    nums = [1, 3, 2, 4]
    print(nums)
    solution.nextPermutation(nums)
    print(nums)

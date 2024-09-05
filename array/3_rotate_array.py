from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return []

        # k % len(nums) is the number of elements to be rotated
        # the rest of the elements are moved to the left
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    print(nums)

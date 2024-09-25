from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left

        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            return self.search(nums, left, mid)
        else:
            return self.search(nums, mid + 1, right)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1]))
    print(sol.findPeakElement([1,2,1,3,5,6,4]))

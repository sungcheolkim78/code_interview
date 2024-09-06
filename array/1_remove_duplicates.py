from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(i + 1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 1, 2]
    print(solution.removeDuplicates(nums))
    print(nums)

    nums = [1, 1, 2, 3, 4]
    print(solution.removeDuplicates(nums))
    print(nums)

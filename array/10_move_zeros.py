from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        num_zeros = 0
        for i in nums:
            if i == 0:
                num_zeros += 1

        ans = [v for v in nums if v != 0]

        for i in range(num_zeros):
            ans.append(0)

        nums[:] = ans

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        nums[last_non_zero_index:] = [0] * (len(nums) - last_non_zero_index)


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes2(nums)
    print(nums)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        # create a dict to store the index of the number
        num_dict = {target - nums[i]: i for i in range(len(nums))}

        # search for the index of the number in the dict
        for i in range(len(nums)):
            if nums[i] in num_dict and i != num_dict[nums[i]]:
                return [i, num_dict[nums[i]]]

        return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))

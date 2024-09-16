from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                return res

            res_two_sum = self.twoSum(nums[i+1:], target=-nums[i])
            for res_two_sum_i in res_two_sum:
                res_three_sum = [nums[i]] + res_two_sum_i
                if res_three_sum not in res:
                    res.append(res_three_sum)

        return res

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        target_dict = {target - nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            if nums[i] in target_dict and i < target_dict[nums[i]]:
                res.append([nums[i], target - nums[i]])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0]))
    print(s.threeSum([0, 0]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([1, 0, -1]))
    print(s.threeSum([1, 0, -1, 0, -1]))
    print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

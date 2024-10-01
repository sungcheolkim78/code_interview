from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)

        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]) -> None:
        seen = set()
        j = i + 1

        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0]))
    print(s.threeSum([0, 0]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([1, 0, -1]))
    print(s.threeSum([1, 0, -1, 0, -1]))
    print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

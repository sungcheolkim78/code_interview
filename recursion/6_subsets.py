from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = [[]]
        for num in nums:
            new_subsets = []
            for curr in output:
                temp = curr.copy()
                temp.append(num)
                new_subsets.append(temp)

            for curr in new_subsets:
                output.append(curr)

        return output

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])

        return output


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets2(nums))

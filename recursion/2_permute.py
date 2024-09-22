from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr: List[int]):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([0, 1]))
    print(solution.permute([1, 2, 3]))
    print(solution.permute([1, 2, 3, 4]))

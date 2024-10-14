from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub_sum = sum(nums[i:j])
                if sub_sum == k:
                    count += 1

        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        cum_sum = [0]
        for i in range(n):
            cum_sum.append(cum_sum[-1] + nums[i])

        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if cum_sum[j] - cum_sum[i] == k:
                    count += 1

        return count

    def subarraySum3(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        dict_cumsum = {}
        curr_sum = 0

        for i in range(n):
            curr_sum += nums[i]
            if curr_sum == k:
                count += 1

            if curr_sum - k in dict_cumsum:
                count += dict_cumsum[curr_sum -k]

            if curr_sum in dict_cumsum:
                dict_cumsum[curr_sum] += 1
            else:
                dict_cumsum[curr_sum] = 1

        return count


if __name__ == '__main__':
    sol = Solution()
    nums, k = [1, 1, 1], 2
    print(sol.subarraySum3(nums, k))

    nums, k = [1, 2, 3], 3
    print(sol.subarraySum3(nums, k))

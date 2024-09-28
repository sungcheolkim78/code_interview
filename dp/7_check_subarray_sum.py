from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        mod_seen = {0: -1}
        prefix_mod_list = []

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            prefix_mod_list.append(prefix_mod)

            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    print(prefix_mod_list)
                    return True
            else:
                mod_seen[prefix_mod] = i

        print(prefix_mod_list)
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkSubarraySum([23,2,4,6,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7,2], 13))

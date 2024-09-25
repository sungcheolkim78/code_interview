from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []

        for num in nums1:
            seen[num] = 1

        for num in nums2:
            if num in seen and seen[num] == 1:
                result.append(num)
                seen[num] = 0

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))
    print(sol.intersection([4,9,5], [9,4,9,8,4]))

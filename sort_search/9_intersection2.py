from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counter = {}
        result = []

        for num in nums2:
            counter[num] = counter.get(num, 0) + 1

        for num in nums1:
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersect([1,2,2,1], [2,2]))
    print(sol.intersect([4,9,5], [9,4,9,8,4]))

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]
        i, j = 0, 0

        for p in range(n + m):
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[p] = nums1_copy[i]
                i += 1
            else:
                nums1[p] = nums2[j]
                j += 1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge2(nums1, 3, nums2, 3)
    print(nums1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def shifted_binary_search(pivot_index, target):
            shift = n - pivot_index
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[(mid - shift) % n] == target:
                    return (mid - shift) % n
                elif nums[(mid - shift) %n] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        return shifted_binary_search(mid, target)


if __name__ == '__main__':
    sol = Solution()
    nums = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    target = 5
    print(sol.search(nums, target))

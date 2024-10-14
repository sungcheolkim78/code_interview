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

        print(mid, nums)

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

    def search2(self, nums: List[int], target: int) -> int:
            n = len(nums)

            # find pivot
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1

            pivot_index = mid
            rotated_nums = nums[pivot_index:] + nums[:pivot_index]

            print(pivot_index, rotated_nums)

            # binary search
            first, last = 0, n - 1
            while first <= last:
                mid = first + (last - first) // 2
                if rotated_nums[mid] == target:
                    return (mid + pivot_index) % n
                elif rotated_nums[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1

            return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(sol.search(nums, target))
    print(sol.search2(nums, target))

    nums = [5, 1, 3]
    target = 5
    print(sol.search(nums, target))
    print(sol.search2(nums, target))

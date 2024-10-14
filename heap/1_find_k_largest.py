import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)

        return -heap[0]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 5
    print(solution.findKthLargest(nums, k))

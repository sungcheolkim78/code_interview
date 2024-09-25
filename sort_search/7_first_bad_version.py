class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


def isBadVersion(version: int) -> bool:
    return version >= bad_version


bad_version = 4

if __name__ == '__main__':
    sol = Solution()
    print(sol.firstBadVersion(5))
    print(sol.firstBadVersion(4))

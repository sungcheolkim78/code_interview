from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert digits to int
        value = 0
        for v in digits:
            value = 10 * value + v

        value += 1

        # convert int to digits
        digits = []
        while value > 0:
            value, r = value // 10, value % 10
            digits.append(r)

        digits.reverse()
        return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([9, 9, 9]))

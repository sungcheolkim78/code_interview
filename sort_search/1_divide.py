MAX_INT = 2 ** 31 - 1
MIN_INT = - 2 ** 31
HALF_MIN_INT = - 2 ** 30

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while dividend <= divisor:
            quotient -= 1
            dividend -= divisor

        if negatives != 1:
            quotient = -quotient

        return quotient

    def divide2(self, dividend: int, divisor: int) -> int:
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while divisor >= dividend:
            power_of_two = -1
            value = divisor

            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                power_of_two += power_of_two
            print(value, power_of_two)

            quotient += power_of_two
            dividend -= value

        return -quotient if negatives != 1 else quotient

    def divide3(self, dividend: int, divisor: int) -> int:
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        max_bit = 0
        while divisor >= HALF_MIN_INT and divisor + divisor >= dividend:
            max_bit += 1
            divisor += divisor

        quotient = 0
        for bit in range(max_bit, -1, -1):
            if divisor >= dividend:
                quotient -= 1 << bit
                dividend -= divisor
            divisor = (divisor + 1) >> 1
            print(bit, divisor, dividend)

        return -quotient if negatives != 1 else quotient


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide3(10, 3))
    print(sol.divide3(-7, 3))
    print(sol.divide3(2 ** 20, -3))
    print(sol.divide3(2 ** 20, 3))

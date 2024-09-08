class Solution:
    def reverse(self, x: int) -> int:
        negative = -1 if x < 0 else 1
        x *= negative

        reverse_digits = []
        while x > 0:
            x, r = x // 10, x % 10
            reverse_digits.append(r)

        v = []
        ten_pow = 1
        while reverse_digits:
            v.append(ten_pow * reverse_digits.pop())
            ten_pow *= 10

        return negative * sum(v)


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))

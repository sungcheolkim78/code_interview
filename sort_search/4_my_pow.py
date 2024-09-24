class Solution:
    def binary_exp(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.binary_exp(x, -n)
        if n % 2 == 1:
            return x * self.binary_exp(x * x, (n - 1) // 2)
        else:
            return self.binary_exp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binary_exp(x, n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(2.0, 10))
    print(sol.myPow(10, 9))

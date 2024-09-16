class Solution:
    def myAtoi(self, s: str) -> int:
        # step 1 - remove whitespace
        s = s.strip()

        if len(s) == 0:
            return 0

        # step 2 - check sign
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        # step 3 - create integer digit list
        digit_map = {f"{v:d}": v for v in range(10)}
        digits = []
        for c in s:
            if c.isnumeric():
                digits.append(digit_map[c])
            else:
                break

        if len(digits) == 0:
            return 0

        # step 4 - convert to integer
        ten_pow = 1
        value = 0
        for v in digits[::-1]:
            value += v * ten_pow
            ten_pow *= 10

        # step 5 - check overflow
        if sign > 0 and value > 2 ** 31 - 1:
            value = 2 ** 31 - 1
        if sign < 0 and value > 2 ** 31:
            value = 2 ** 31

        return value * sign


if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("-91283472332"))
    print(solution.myAtoi("91283472332"))
    print(solution.myAtoi("-91283472332"))
    print(solution.myAtoi("+91283472332"))
    print(solution.myAtoi("   +91283472332"))
    print(solution.myAtoi("   +91283472332   "))
    print(solution.myAtoi("-+91283472332"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 91283472332"))
    print(solution.myAtoi("-91283472332.323"))
    print(solution.myAtoi("-91283472332.323"))

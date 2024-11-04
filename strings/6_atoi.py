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

    def myAtoi2(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        while index < n and s[index] == " ":
            index += 1

        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1

        while index < n and s[index].isdigit():
            digit = int(s[index])

            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            index += 1

        return result * sign


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

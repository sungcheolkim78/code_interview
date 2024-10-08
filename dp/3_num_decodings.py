class Solution(object):
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            two_digits = int(s[i - 2:i])
            if two_digits >= 10 and two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('12'))
    print(s.numDecodings('226'))
    print(s.numDecodings('0'))
    print(s.numDecodings('06'))
    print(s.numDecodings('00'))
    print(s.numDecodings('01'))
    print(s.numDecodings('212526'))

from typing import List


class Solution:
    def isMatch0(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        return first_match and self.isMatch0(s[1:], p[1:])

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch2(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == "*":
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[(i, j)] = ans
            return memo[i, j]

        return dp(0, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch0("aa", "a"))
    print(solution.isMatch0("aa", "a."))
    print(solution.isMatch2("ab", ".*"))
    print(solution.isMatch2("aa", "a."))
    print(solution.isMatch2("aa", "a*"))
    print(solution.isMatch2("aabc", "a*b."))

from typing import List
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True

            return False

        return dp(len(s) - 1)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        print(words)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak2('leetcode', ['leet', 'code']))
    print(sol.wordBreak2('applepenapple', ['apple', 'pen']))
    print(sol.wordBreak2('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))

from typing import List

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return ns + 1 == nt


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("a", "a"),
        ("a", "b"),
        ("ab", "ab"),
        ("ab", "ac"),
        ("ab", "aa"),
        ("aad", "aa"),
        ("aa", "aba"),
        ("aaaccdx", "aacacdx"),
        ("aaa", "aaa"),
    ]
    for s, t in samples:
        print(f"{s} ~ {t}: {sol.isOneEditDistance(s, t)}")

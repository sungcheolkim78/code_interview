class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # approach with two index i for haystack, j for needle
        i, j = 0, 0

        # check size
        n_needle, n_hay = len(needle), len(haystack)
        if n_needle > n_hay:
            return -1

        # compare needle with string starts at i
        for i in range(n_hay - n_needle + 1):
            if haystack[i:i + n_needle] == needle:
                return i

        return -1


if __name__ == '__main__':
    print(Solution().strStr('hello', 'll'))
    print(Solution().strStr('aaaaaaaaaa', 'bba'))
    print(Solution().strStr('aaaaabbbbb', 'aaaa'))
    print(Solution().strStr('aaaaabbbbb', 'aabb'))
    print(Solution().strStr('aaaaaaaaaa', ''))

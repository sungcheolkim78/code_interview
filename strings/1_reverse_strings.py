from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        num = len(s)

        if num == 0:
            return

        for i in range(num // 2):
            s[i], s[num - i - 1] = s[num - i - 1], s[i]

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        new = []
        for _ in range(len(s)):
            new.insert(0, s.pop(0))

        s[:] = new


if __name__ == '__main__':
    solution = Solution()

    s = ['h', 'e', 'l', 'l', 'o']
    solution.reverseString(s)
    print(s)

    s = ['H', 'a', 'n', 'n', 'a', 'h']
    solution.reverseString(s)
    print(s)

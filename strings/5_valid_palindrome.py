class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up string
        clean_chars = [c.lower() for c in s if c.isalnum()]

        s = ''.join(clean_chars)
        n = len(s)

        # single char is Palindrome
        if n <= 1:
            return True

        # check Palindrome
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome("raceacar"))
    print(s.isPalindrome(""))
    print(s.isPalindrome("aba"))

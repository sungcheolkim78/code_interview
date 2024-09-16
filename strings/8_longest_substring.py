class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        char_set = set()
        left = 0

        for right in range(n):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("dvdf"))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("a"))

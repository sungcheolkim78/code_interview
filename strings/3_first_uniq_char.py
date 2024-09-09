class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count the frequency of each char
        count_dict = {}
        for c in s:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1

        # find the first char that appears only once
        uniq_char = None
        for k, v in count_dict.items():
            if v == 1:
                uniq_char = k
                break

        if uniq_char is None:
            return -1

        return s.find(uniq_char)


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("leetcodeleetcode"))
    print(s.firstUniqChar("loveleetcodeleetcode"))
    print(s.firstUniqChar("ll"))
    print(s.firstUniqChar(""))
    print(s.firstUniqChar("oooooooooooooooooooooooooooooooooooooooooooooooo"))

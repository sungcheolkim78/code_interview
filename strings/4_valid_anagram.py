class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check count
        if len(s) != len(t):
            return False

        # count occurrance
        def count_dict(s: str):
            out = {}
            for c in s:
                if c in out:
                    out[c] += 1
                else:
                    out[c] = 1
            return out

        count_dict1 = count_dict(s)
        count_dict2 = count_dict(t)

        # compare count dictionary
        for k, v in count_dict1.items():
            if k not in count_dict2:
                return False
            if count_dict2[k] != v:
                return False

        return True



if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
    print(s.isAnagram("a", "aa"))
    print(s.isAnagram("aa", "a"))
    print(s.isAnagram("aa", "ab"))

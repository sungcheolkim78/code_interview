class Solution:
    def romanToInt(self, s: str) -> int:
        double_dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        single_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i: i+2] in double_dict:
                num += double_dict[s[i: i+2]]
                i += 2
            else:
                num += single_dict[s[i]]
                i += 1

        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))

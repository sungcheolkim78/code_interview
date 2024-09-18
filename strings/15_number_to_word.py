from typing import List


class Solution:
    number_to_words_map = {
        1_000_000_000: "Billion",
        1_000_000: "Million",
        1_000: "Thousand",
        100: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        for v, word in self.number_to_words_map.items():
            if num >= v:
                prefix = (self.numberToWords(num // v) + " ") if num >= 100 else ""

                unit = word

                suffix = "" if num % v == 0 else " " + self.numberToWords(num % v)

                return prefix + unit + suffix


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberToWords(0))
    print(solution.numberToWords(1))
    print(solution.numberToWords(123))
    print(solution.numberToWords(12345))
    print(solution.numberToWords(1234567890))
    print(solution.numberToWords(1000000000))
    print(solution.numberToWords(1000000001))
    print(solution.numberToWords(1000000010))

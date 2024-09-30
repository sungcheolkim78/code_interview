from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter()

        for i in range(len(s2)):
            s2_counter[s2[i]] += 1

            if i >= len(s1):
                if s2_counter[s2[i - len(s1)]] == 1:
                    del s2_counter[s2[i - len(s1)]]
                else:
                    s2_counter[s2[i - len(s1)]] -= 1

            if s2_counter == s1_counter:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))
    print(solution.checkInclusion("ab", "eidboaoo"))

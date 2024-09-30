from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_counter = Counter(p)
        s_counter = Counter()

        output = []

        for i in range(ns):
            s_counter[s[i]] += 1

            if i >= np:
                if s_counter[s[i - np]] == 1:
                    del s_counter[s[i - np]]
                else:
                    s_counter[s[i - np]] -= 1

            if s_counter == p_counter:
                output.append(i - np + 1)

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))
    print(solution.findAnagrams("abab", "ab"))
    print(solution.findAnagrams("abab", "bab"))

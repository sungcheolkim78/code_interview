from typing import List, DefaultDict, Tuple
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans: DefaultDict[Tuple, List[str]] = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            ans[tuple(count)].append(s)

        return list(ans.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

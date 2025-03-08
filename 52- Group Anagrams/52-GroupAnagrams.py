from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)    
        return list(res.values())

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(input_strs))
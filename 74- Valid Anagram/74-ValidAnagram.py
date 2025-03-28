from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        #           or
        # return sorted(s) == sorted(t)
        #           or
        # if len(s) != len(t): return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0)
        #     countT[t[i]] = 1 + countT.get(t[i],0)
        
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        
        # return True

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))  # Output: True

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))  # Output: False
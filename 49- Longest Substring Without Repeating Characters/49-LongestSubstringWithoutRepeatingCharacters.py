class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

if __name__ == "__main__":
    solution = Solution()
    test_string = "abcabcbb"
    print(test_string)
    print(solution.lengthOfLongestSubstring(test_string))
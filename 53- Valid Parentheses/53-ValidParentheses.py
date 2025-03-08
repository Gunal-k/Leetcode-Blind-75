class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{","]":"[",")":"("}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    test_string = "()[]{}"
    print(f"Is the string '{test_string}' valid? {solution.isValid(test_string)}")
    test_string = "(]"
    print(f"Is the string '{test_string}' valid? {solution.isValid(test_string)}")
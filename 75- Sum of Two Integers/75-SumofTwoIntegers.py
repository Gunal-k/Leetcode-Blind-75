class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        if a > MAX_INT:
            a = ~(a ^ MASK)

        return a

# Test the function
if __name__ == "__main__":
    solution = Solution()
    a = 5
    b = 3
    print(f"The sum of {a} and {b} is: {solution.getSum(a, b)}")
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r, l = len(matrix)-1, 0 
        
        while l < r:
            for i in range(r-l):
                t, b = l, r

                # Save the top-left value
                topLeft = matrix[t][l+i]
                # Move bottom-left to top-left
                matrix[t][l+i] = matrix[b-i][l]
                # Move bottom-right to bottom-left
                matrix[b-i][l] = matrix[b][r-i]
                # Move top-right to bottom-right
                matrix[b][r-i] = matrix[t+i][r]
                # Assign saved top-left to top-right
                matrix[t+i][r] = topLeft
            # Move the right boundary left
            r -= 1
            # Move the left boundary right
            l += 1

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    Solution().rotate(matrix)
    
    print("\nRotated matrix:")
    for row in matrix:
        print(row)
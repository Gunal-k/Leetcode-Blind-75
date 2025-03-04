from typing import List

# Original solution starts here
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowzero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowzero:
            for c in range(cols):
                matrix[0][c] = 0

# Original solution ends here

def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)

if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    print("Original matrix:")
    print_matrix(matrix)
    
    solution = Solution()
    solution.setZeroes(matrix)
    
    print("\nMatrix after calling setZeroes:")
    print_matrix(matrix)
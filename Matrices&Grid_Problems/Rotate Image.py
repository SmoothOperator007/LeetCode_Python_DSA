"""
Problem: Rotate Image
Difficulty: Medium

--- METHOD 1: OPTIMAL IN-PLACE APPROACH (Transpose + Reverse) ---
Intuition & Key Learnings:
To rotate a matrix 90 degrees clockwise without using extra space, we break it into two simple geometric steps:

1. Transpose the Matrix (Swap across the main diagonal):
   - Code: for j in range(i + 1, n)
   - Why start j at i + 1?: If you started j at 0 every time, you would swap elements across the diagonal and then swap them RIGHT BACK (undoing your work!). 
     Starting j at i + 1 ensures we only swap the upper triangle with the lower triangle once.

2. Reverse Each Row:
   - Flipping each row horizontally after transposing completes the 90-degree clockwise rotation.

Complexity:
- Time Complexity: O(n^2)
- Space Complexity: O(1)

--- METHOD 2: EXPLICIT EXTRA SPACE MAPPING APPROACH ---
Intuition & Key Learnings:
When in-place index manipulation and diagonal boundaries become too confusing during an interview:
1. Make a deep backup copy of the grid manually using nested loops.
2. Read from the frozen copy and map each coordinate directly to its rotated destination using:
    matrix[j][n - 1 - i] = copy_matrix[i][j]

Why this works:
- Reading from an unchanged copy_matrix prevents values from overwriting each other mid-way.
- The original row index (i) gets inverted and shifted to the right column (n - 1 - i), while the column (j) becomes the new row.

Complexity:
- Time Complexity: O(n^2)
- Space Complexity: O(n^2)
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # ==========================================
        # METHOD 1: Optimal In-Place (Transpose + Reverse)
        #==========================================
        n = len(matrix)
        
        # Transpose: j starts at i + 1 to avoid swapping elements back and forth
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row horizontally
        for i in range(n):
            matrix[i].reverse()


        # ==========================================
        # METHOD 2: Explicit Extra Space Mapping Approach
        # ==========================================
        n = len(matrix)
        
        copy_matrix = []
        for row in matrix:
            new_row = []
            for i in range(n):
                new_row.append(row[i])
            copy_matrix.append(new_row)
        
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = copy_matrix[i][j]
        
        return matrix

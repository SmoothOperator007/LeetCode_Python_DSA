"""
Problem: 54. Spiral Matrix (Medium)

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Boundary Simulation (Layer-by-Layer Peeling)
Intuition: 
Instead of tracking visited cells with a separate boolean matrix or navigating using complex directional state machines, 
we maintain four boundary pointers: `top`, `bottom`, `left`, and `right`. 
We traverse the perimeter in four fixed directions (top row left-to-right, right column top-to-bottom, bottom row right-to-left, and left column bottom-to-top), 
shrinking the corresponding boundary inward after each complete pass.

Time Complexity: O(m * n), where m and n are the dimensions of the matrix, as every single element is visited exactly once.
Space Complexity: O(1) auxiliary space (excluding the output array `res`).

--- LEARNING ---
- Boundary Convergence: Utilizing conditional checks (`if top <= bottom:` and `if left <= right:`) before the bottom and left traversals prevents 
  duplicate element processing when the matrix collapses into a single remaining row or column.
- Index Offsets: Using inclusive boundaries (`len(matrix) - 1`) combined with Python's exclusive upper bounds in `range(start, stop + 1)` 
  keeps index calculations intuitive and avoids `IndexError`.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
            
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse Top row (left to right)
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            
            # 2. Traverse Right column (top to bottom)
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            
            # 3. Traverse Bottom row (right to left)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
            bottom -= 1
                
            # 4. Traverse Left column (bottom to top)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
            left += 1
                
        return res

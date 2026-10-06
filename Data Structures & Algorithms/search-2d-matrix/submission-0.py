class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        left = 0
        right = row * column - 1
        
        
        
        while left <= right:
            mid = (left + right) // 2
            mid_col = mid % column 
            mid_row = mid // column 
            if matrix[mid_row][mid_col] < target:
                left = mid + 1
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            elif matrix[mid_row][mid_col] == target:
                return True
        return False


        
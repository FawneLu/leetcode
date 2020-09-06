class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        
        n = len(matrix[0])
        left = 0
        right = len(matrix)*len(matrix[0])-1
        
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            if matrix[mid // n][mid % n] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
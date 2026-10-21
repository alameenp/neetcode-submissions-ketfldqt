class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        columns = len(matrix[0])-1
        while left <= right:
            mid_row = (left+right)//2
            if matrix[mid_row][0] > target:
                right = mid_row - 1
                continue
            
            elif matrix[mid_row][columns] < target:
                left = mid_row+1
                continue
            
            else:
                l = 0
                r = columns
                while l<=r:
                    mid = (l+r)//2
                    print(mid_row, mid)
                    if matrix[mid_row][mid]==target:
                        return True
                    elif matrix[mid_row][mid] > target:
                        r = mid-1
                    else:
                        l = mid+1
            return False
        return False



        
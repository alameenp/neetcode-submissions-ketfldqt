class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        column_check = {}
        grid_check = {}

        for row_num,row in enumerate(board):
            row_check = set()
            grid_row = (row_num//3)*3
            grid_row_index = str(grid_row)
            for column,element in enumerate(row):
                if element == '.':
                    continue 
                if (element in row_check):
                    return False
                
                if column_check.get(column) is None:
                    column_check[column]=set()
                
                if (element in column_check[column]):
                    return False

                grid_column_index = str((column//3)*3)
                grid_index = grid_row_index+grid_column_index

                if grid_check.get(grid_index) is None:
                    grid_check[grid_index] = set()
                
                if (element in grid_check[grid_index]):
                    return False
                
                column_check[column].add(element)
                row_check.add(element)
                grid_check[grid_index].add(element)
        return True




        
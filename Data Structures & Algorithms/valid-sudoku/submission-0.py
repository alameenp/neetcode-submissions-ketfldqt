class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_row = [set() for i in range(9)]
        list_column = [set() for i in range(9)]
        list_grid = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                grid_index = (i//3)*3+(j//3)

                if val in list_row[i]:
                    return False
                list_row[i].add(board[i][j])
                
                if val in list_column[j]:
                    return False
                list_column[j].add(val)

                if val in list_grid[grid_index] :
                    return False
                list_grid[grid_index].add(val)
        
        return True


        


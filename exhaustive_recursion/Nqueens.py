
def solveNQueens(n):
    board = [["."]*n for i in range(n)]

    res = []
    def backtrack(current_row):
        if current_row == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        
        for current_col in range(n):
            legal = True
            for previous_row in range(current_row): #iterate through the previous rows
                column_of_previous_queen = board[previous_row].index("Q")
                if column_of_previous_queen == current_col:
                    legal = False
                # check diagonal above to the right
                if column_of_previous_queen == current_col + current_row - previous_row:
                    legal = False

                if column_of_previous_queen == current_col - current_row + previous_row:
                    legal = False

            if legal:
                board[current_row][current_col] = "Q"
                print(board)
                backtrack(current_row+1)
                board[current_row][current_col] = "."

    backtrack(0)
    return res

print(solveNQueens(4))
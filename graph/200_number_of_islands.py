from collections import deque
def numIslands(grid) -> int:
    q = deque([])
    visited = set()
    count = 0 

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = (row, col)
            if cell not in visited and grid[row][col] == "1":
                q.appendleft(cell)
                count+=1
                while q:
                    currentCell = q.pop()
                    visited.add(currentCell)
                    row = currentCell[0]
                    col = currentCell[1]
                    #check down
                    if row + 1 < len(grid) and grid[row+1][col] == "1":
                        if (row+1, col) not in visited:
                            q.appendleft((row+1,col))
                    #check up
                    if row - 1 >= 0 and grid[row-1][col] == "1":
                       if (row-1, col) not in visited:
                           q.appendleft((row-1,col))
                    #check left
                    if col - 1 >= 0 and grid[row][col-1] == "1":
                       if (row, col-1) not in visited:
                           q.appendleft((row,col-1))
                    #check right
                    if col + 1 < len(grid[0]) and grid[row][col+1] == "1":
                       if (row, col+1) not in visited:
                           q.appendleft((row,col+1))
            
    return count

numIslands([["1", "1", "1", ], ["0", "1", "0"], ["1", "1", "1"]])
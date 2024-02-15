def minimum_island(grid):
  visited = set()
  n_rows = len(grid)
  n_cols = len(grid[0])
  min_size = n_rows*n_cols
  # need to iterate through every row and column of grid
  # start at the top left
  r, c = 0, 0
  # we need a stack to do a DFS
  for r in range (n_rows):
    for c in range(n_cols):
        # then we need to do a DFS of the grid
        if (r, c) in visited:
          continue
        cell = grid[r][c]
        visited.add((r,c))
        if cell == "L":
          stack = []
          stack.append((r,c))
          current_size = 0
          while len(stack)>0:
            #populate the stack
            # add the cell above handling limits
            r, c = stack.pop()
            visited.add((r,c))
            current_size+=1
            if r > 0:
              up = (r-1, c)
              if (up not in visited) and "L"==grid[up[0]][up[1]]:
                stack.append(up)
            # add the cell down, handling out of bounds
            if r < n_rows - 1:
              down = (r+1, c)
              if (down not in visited) and "L"==grid[down[0]][down[1]]:
                stack.append(down)
            # add left
            if c > 0:
              left = (r, c-1)
              if (left not in visited) and ("L"==grid[left[0]][left[1]]):
                stack.append(left)
            if c < n_cols -1:
              right=(r, c+1)
              if (right not in visited) and ("L"==grid[right[0]][right[1]]):
                stack.append(right)
            if len(stack)==0:    
              if current_size<min_size:
                min_size=current_size
            
  return min_size

if __name__ == "__main__":
  grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

  print(minimum_island(grid))

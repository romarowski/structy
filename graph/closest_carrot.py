"""
closest carrot

Write a function, closest_carrot, that takes in a grid, a starting row, 
and a starting column. In the grid, 'X's are walls, 'O's are open
spaces, and 'C's are carrots. The function should return a number 
representing the length of the shortest path from the starting position 
to a carrot. You may move up, down, left, or right, but 
cannot pass through walls (X). 
If there is no possible path to a carrot, then return -1.
"""

from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    visited = set((starting_row, starting_col))

    q = deque([])
    q.append((starting_row, starting_col, 0))

    deltas = [(1, 0), (-1,0), (0, 1), (0, -1)]

    while len(q) > 0:
        r, c, dist = q.popleft()

        if grid[r][c] == "C":
            return dist
        
        for delta in deltas:
            neighbor_row = r + delta[0]
            neighbor_col = c + delta[1]

            inbound_row = 0 <= neighbor_row < len(grid)
            inbound_col = 0 <= neighbor_col < len(grid[0])

            if inbound_row and inbound_col:
                pos = (neighbor_row, neighbor_col)
                if pos not in visited:
                    if grid[neighbor_row][neighbor_col] != "X":
                        q.append((
                            neighbor_row,
                            neighbor_col,
                            dist+1
                        ))
                        visited.add(pos)
    return -1

grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'O', 'X', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4
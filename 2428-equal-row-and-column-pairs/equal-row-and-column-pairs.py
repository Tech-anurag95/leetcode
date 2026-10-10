class Solution:
  def equalPairs(self, grid: list[list[int]]) -> int:
    count=0
    for i in range(len(grid[0])):
        a=[]
        for j in range(len(grid)):
            a.append(grid[j][i])
        for row in grid:
            if a==row:
                count += 1
    return count


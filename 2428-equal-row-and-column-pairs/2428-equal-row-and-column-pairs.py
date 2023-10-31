class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        l = []
        for i, row in enumerate(grid):
            for y in range(len(grid[0])):
                col = [grid[i][y] for i in range(len(grid))]
                if (row == col) :
                    l.append(row)
        return len(l)
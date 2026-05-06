class Solution:
    def Zeros(self, i, j, row, column, grid):
        if i < 0 or i >= row or j < 0 or j >= column:
            return
        if grid[i][j] == "0":
            return
        
        grid[i][j] = "0"

        self.Zeros(i - 1, j, row, column, grid)
        self.Zeros(i + 1, j, row, column, grid)
        self.Zeros(i, j + 1, row, column, grid)
        self.Zeros(i, j - 1, row, column, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        column = len(grid[0])

        for i in range(row):
            for j in range(column):
                    if grid[i][j] == "1":
                        count += 1
                        self.Zeros(i, j , row, column, grid)

        return count
import sys
sys.setrecursionlimit(10**8)


class Solution:
    def numIslands(self, grid):
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i > 0 and j < len(grid) and grid[i-1][j] == 0 and grid[i][j-1] == 0 and grid[i-1][j-1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0 and grid[i][j+1] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j+1] == 0:
                    numOfIslands += 1
                if i - 1 == 0 and grid[i][j-1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0 and grid[i][j+1] == 0:
                    numOfIslands += 1

                if j+1 == len(grid)-1 and grid[i-1][j] == 0 and grid[i][j-1] == 0 and grid[i-1][j-1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0 and grid[i][j+1] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j+1] == 0:
                    numOfIslands += 1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends

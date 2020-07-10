'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''


class Solution(object):

    def minPathSum(self, grid):
        l = len(grid)
        dp = [0 for i in range(l)]
        for i in range(l):
            dp[i] = [0 for i in range(len(grid[i]))]
        result = 2 ** 31 - 1
        dp[0][0] = grid[0][0]
        for i in range(l):
            for j in range(len(grid[i])):
                if j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif j != 0 and i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j != 0 and i != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[l-1][len(dp[l-1])-1]


if __name__ == '__main__':
    a = Solution()
    print(a.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))

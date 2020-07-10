'''
给定一个三角形，找出自顶向下的最小路径和。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

dp[i][j] : 表示包含第i行j列元素的最小路径和
我们很容易想到可以自顶向下进行分析。并且，无论最后的路径是哪一条，它一定要经过最顶上的元素，即[0,0]。所以我们需要对dp[0][0]进行初始化。

dp[0][0] = [0][0]位置所在的元素值
继续分析，如果我们要求dp[i][j]，那么其一定会从自己头顶上的两个元素移动而来
'''


class Soultion(object):

    def minmumTotal(self, triangle):
        l = len(triangle)
        if l < 1:
            return 0
        if l == 1:
            return triangle[0][0]
        dp = [0 for i in range(l)]
        for i in range(l):
            dp[i] = [0 for i in range(len(triangle[i]))]
        print(dp)
        result = 2 ** 31 - 1
        dp[0][0] = triangle[0][0]
        dp[1][1] = triangle[1][1] + triangle[0][0]
        dp[1][0] = triangle[1][0] + triangle[0][0]
        for i in range(2, l):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]  # 最左边的元素只能从自己头顶而来
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]  # 最右边的元素只能从自己左上角而来
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        for i in dp[len(dp) - 1]:
            result = min(result, i)
        return result


if __name__ == '__main__':
    a = Soultion()
    print(a.minmumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))

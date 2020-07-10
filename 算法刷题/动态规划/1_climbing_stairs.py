# coding:utf-8
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2输出： 2解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3输出： 3解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

通过分析我们可以明确，该题可以被分解为一些包含最优子结构的子问题，即它的最优解可以从其子问题的最优解来有效地构建。
满足“将大问题分解为若干个规模较小的问题”的条件。所我们令 dp[n] 表示能到达第 n 阶的方法总数，可以得到如下状态转移方程：
dp[n]=dp[n-1]+dp[n-2]

'''


class Solution(object):

    def climbing_stairs(self, n):
        if n == 1:
            return 1
        dp = [0 for i in range(n+1)]
        print(dp)
        dp[1] = 1
        dp[2] = 2
        print(dp)
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp)
        return dp[n]


if __name__ == '__main__':
    a = Solution()
    print(a.climbing_stairs(5))

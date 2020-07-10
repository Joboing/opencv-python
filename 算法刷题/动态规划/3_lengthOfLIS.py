'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。

要找的是最长上升子序列（Longest Increasing Subsequence，LIS）。因为题目中没有要求连续，
所以LIS可能是连续的，也可能是非连续的。同时，LIS符合可以从其子问题的最优解来进行构建的条件。
所以我们可以尝试用动态规划来进行求解。首先我们定义状态：

dp[i] ：表示以nums[i]结尾的最长上升子序列的长度
'''


class Solution(object):

    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return 0
        dp = [0 for i in range(len(nums))]
        result = 1
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(len(nums)):
                if j < i:
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[j] + 1, dp[i])
            result = max(result, dp[i])
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

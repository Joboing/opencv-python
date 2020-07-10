'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
分析：
dp[i]：表示以 nums[i] 结尾的连续子数组的最大和。
如果要得到dp[i]，那么nums[i]一定会被选取。并且 dp[i] 所表示的连续子序列与 dp[i-1] 所表示的连续子序列很可能就差一个 nums[i] 。即
dp[i] = dp[i-1]+nums[i] , if (dp[i-1] >= 0)
但是这里我们遇到一个问题，很有可能dp[i-1]本身是一个负数。那这种情况的话，如果dp[i]通过dp[i-1]+nums[i]来推导，那么结果其实反而变小了，
因为我们dp[i]要求的是最大和。所以在这种情况下，如果dp[i-1]<0，那么dp[i]其实就是nums[i]的值。即
dp[i] = nums[i] , if (dp[i-1] < 0)
综上分析，我们可以得到：
dp[i]=max(nums[i], dp[i−1]+nums[i])

时间复杂度：O(N)。空间复杂度：O(N)

'''


class Solution(object):

    def maxSubArray(self, nums):
        if len(nums) < 1:
            return 0
        dp = [0 for i in range(len(nums))]
        result = nums[0]
        dp[0] = nums[0]#设置初始值
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(dp[i], result)
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

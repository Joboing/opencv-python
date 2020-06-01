class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([1, 8, 9, 6, 2], 10))

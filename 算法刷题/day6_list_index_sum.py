class Solution(object):
    def pivotIndex(self, mylist):
        length = len(mylist)
        mid_flag = False
        for i in range(1, length - 1):
            if sum(mylist[:i]) == sum(mylist[i + 1:]):
                mid_flag = True
                return i
        if not mid_flag:
            return -1


if __name__ == '__main__':
    a = Solution()
    print(a.pivotIndex([1, 2, 3]))

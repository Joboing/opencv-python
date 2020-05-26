'''
选择排序

'''


class Solution(object):
    def select_sort(self, mylist):
        for i in range(len(mylist) - 1):
            min_index = i
            for j in range(i + 1, len(mylist)):
                if mylist[j] < mylist[min_index]:
                    min_index = j
            if i != min_index:
                mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
        return mylist


if __name__ == '__main__':
    a = Solution()
    print(a.select_sort([1, 2, 6, 4, 3, 2, 1, 7, 5]))

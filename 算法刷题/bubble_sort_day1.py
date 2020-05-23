'''
冒泡排序
优化点：
1.添加有序标记（flag），当没有元素交换时跳出循环
2.记录有序或无序边界，已有序的元素不需要在被进行比较，因此每轮需比较的数列长度会减少
'''


class Solution(object):
    def bubble_sort(self, list):
        for i in range(len(list)):
            for j in range(len(list) - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list

    def bubble_sort_2(self, list):
        n = len(list)
        last_exchange_index = 0   #记录最后一次交换元素的位置
        sort_border = n-1         #无序数列边界
        for i in range(n):
            flag = True           #有序标记，每轮开始初始值均为n
            for j in range(0, sort_border):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    flag = False  #有元素交换，则标记为False
                    last_exchange_index = j
            sort_border = last_exchange_index
            if flag:
                break
        return list
if __name__ == '__main__':
    a = Solution()
    print(a.bubble_sort([1, 3, 5, 2, 4]))

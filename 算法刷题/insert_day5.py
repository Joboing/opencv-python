'''
数组指定位置插入一个元素,不能调用API
'''


class Solution1(object):
    def __init__(self, lst):
        self.len = len(lst)
        self.list1 = lst

    def insert(self, i, e):
        """
        lst：一个数组或向量，Python 就用 list 表达吧
        i：待插入元素的位置
        e：待插入元素
        """
        count = 0
        if i < 0 or i >= self.len:  # 如果插入得索引大于列表长度或小于0，返回索引错误
            print("index error")
        for m in range(self.len - 1, i - 1, -1):
            if self.list1[m] is None:
                count += 1
        if count == 0:
            self.expand()
        for k in range(len(self.list1) - 2, i - 1, -1):
            self.list1[k + 1] = self.list1[k]
        self.list1[i] = e
        return self.list1

    def expand(self):
        list2 = [None for i in range(self.len + 1)]
        for i in range(self.len):
            list2[i] = self.list1[i]
        self.list1 = list2.copy()


class Solution2(object):

    def insert(self, lst, index, value):
        if index < 0 or index >= len(lst) - 1:  # 如果插入得索引大于列表长度或小于0，返回索引错误
            print("index error")
        if index == len(lst):
            return lst + [value]
        else:
            return lst[:index] + [value] + lst[index:]


if __name__ == '__main__':
    a = Solution1([1, 2, 3, 4, 5])
    b = Solution2()
    print(a.insert(2, 8))
    print(b.insert([1, 2, 3, 4, 5], 2, 8))

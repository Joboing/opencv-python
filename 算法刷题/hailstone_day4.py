'''
希尔顿序列的有穷性
n=1,return 1
n>1且为偶数时，{n}并{n/2}
n>1且为奇数时，{n}并{3n+1}

'''


class Solution(object):
    def hailstone(self, n):
        hail_list = []
        length = 1
        while n > 1:
            hail_list.append(n)
            if n % 2:
                n = 3 * n + 1
            else:
                n = n // 2
            length += 1
        else:
            hail_list.append(1)
            length += 1
        return [hail_list, length]


if __name__ == '__main__':
    a = Solution()
    len_list = []
    for i in range(50000):
        len_list.append(a.hailstone(i)[1])
    print(max(len_list))

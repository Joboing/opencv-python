def binary_search(arr, left, right, hkey):
    """
    arr：有序数组
    left：查找区间左侧
    right：查找区间右侧
    hkey：带查找的关键码
    备注：left, right 都包括在内，找不到返回 -1

    """
    middle = (left+right)//2
    if left > right:
        return -1
    if hkey == arr[middle]:
        return middle
    if hkey > arr[middle]:
        return binary_search(arr, middle+1, right,hkey)
    else:
        return binary_search(arr,left, middle-1, hkey)

if __name__ == '__main__':
    print(binary_search([1,2,3,4,5,6,7],0,6,7))
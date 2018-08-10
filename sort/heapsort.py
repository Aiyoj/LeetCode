
def adjustheap(arr, i, length):
    # 取出当前元素
    tmp = arr[i]
    j = 2 * i + 1
    while j < length:
        if j + 1 < length and arr[j] < arr[j + 1]:
            j += 1
        if arr[j] > tmp:
            arr[i] = arr[j]
            i = j
        else:
            break

        arr[i] = tmp
        j = 2 * i + 1


def heapsort(arr):
    length = len(arr)
    # 构建大顶堆(从下至上，从右至左)
    for i in range(length // 2 - 1, -1, -1):
        adjustheap(arr, i, length)
    for i in range(length-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjustheap(arr, 0, i)


if __name__ == '__main__':
    arr = [9, 8, 75, 8, 3, 7, 3, 2, 1]
    heapsort(arr)
    print(arr)


def quicksort(arr, left, right):
    if left > right:
        return None
    tmp = arr[left]
    i = left
    j = right

    while i != j:
        while arr[j] >= tmp and i < j:
            j -= 1
        while arr[i] <= tmp and i < j:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left] = arr[i]
    arr[i] = tmp
    quicksort(arr, left, i - 1)
    quicksort(arr, i + 1, right)


if __name__ == '__main__':
    arr = [3, 5, 2, 6, 1, 4, 9, 6]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)

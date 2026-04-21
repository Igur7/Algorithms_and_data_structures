def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap][0] > temp[0]:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

def shell_sort_knuth(arr):
    n = len(arr)
    gap = 1

    while gap < n // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap][0] > temp[0]:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 3
def subseq(arr, index, current):
    if index == len(arr):
        print(current)
        return

    subseq(arr, index + 1, current + [arr[index]])
    subseq(arr, index + 1, current)


subseq([1, 2, 3], 0, [])
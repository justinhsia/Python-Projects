# This quick sort uses the Lumoto partition algorithm.
# https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def quick_sort(arr, lo, hi):
    if len(arr) == 1:
        return

    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort(arr, lo, p-1)
        quick_sort(arr, p+1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    pivot_index = lo

    for i in range(lo, hi):
        if arr[i] <= pivot:    
            swap(i, pivot_index, arr)
            pivot_index += 1

    swap(pivot_index, hi, arr)

    return pivot_index


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
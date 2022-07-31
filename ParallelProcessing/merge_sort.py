import random
import time
import multiprocessing


def merge(arr,l,m,r):
    size1 = m-l+1
    size2 = r-m
    L = arr[l:m+1]
    R = arr[m:r]
    i = 0
    j = 0
    k = l
    while i < size1 and j < size2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < size1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < size2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def multi_mergeSort(arr, l, r, level):
    if l < r:
        m = (l + (r - 1)) // 2
        if level<2 :
            p1 = multiprocessing.Process(target=multi_mergeSort, args=(arr, l, m, level+1))
            p2 = multiprocessing.Process(target=multi_mergeSort, args=(arr, m + 1, r, level+1))
        else :
            p1 = multiprocessing.Process(target=mergeSort, args=(arr, l, m))
            p2 = multiprocessing.Process(target=mergeSort, args=(arr, m + 1, r))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        merge(arr, l, m, r)

if __name__ == '__main__':
    n = 1000000
    arr = [random.randint(0, i * 100) for i in range(n)]
    start = time.perf_counter()
    # mergeSort(arr, 0, n - 1)
    multi_mergeSort(arr, 0, n - 1, 0)
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 5)}')

    #https://youtu.be/Tn0u-IIBmtc
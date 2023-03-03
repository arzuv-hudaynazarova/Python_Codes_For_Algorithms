import random
import time

# Öncelikle, rastgele bir 10000 sayı oluşturacağız:
arr = [random.randint(1, 1000) for i in range(10000)]

# Daha sonra, birleştirme (merge sort) sıralaması uygulayacağız:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# BruteForce sırama algoritması
def BruteForceSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



#Sıralama süresi, aşağıdaki gibi karşılaştırılır:

# 1.  Merge Sort algoritması ile sıralama ve çalışma süresinin ölçülmesi
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()
print("MergeSort çalışma süresi: ", end_time - start_time, "saniye")

# 2. BruteForce algoritması ile sıralama ve çalışma süresinin ölçülmesi
start = time.time()
BruteForceSort(arr)
end = time.time()
print("BruteForce çalışma süresi:", end-start, "saniye")


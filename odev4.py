import random
import time

# Merge Sort Algoritması:
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


# Quick Sort Algoritması:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

# BruteForce Sıralama Algoritması:
def BruteForceSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



# Rastgele 10000 sayılı bir dizi oluşturalım:
arr = [random.randint(1, 1000) for i in range(10000)]


# Sıralama süresi, karşılaştırılması işlemi:

# 1.  Merge Sort algoritması ile sıralama ve çalışma süresinin ölçülmesi
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()
print("Merge Sort çalışma süresi: ", end_time - start_time, "saniye")

# 2.  Quick Sort algoritması ile sıralama ve çalışma süresinin ölçülmesi
start_time = time.time()
sorted_arr1 = quick_sort(arr)
end_time = time.time()
print("Quick Sort çalışma süresi: ", end_time - start_time, "saniye")


# 3.  BruteForce algoritması ile sıralama ve çalışma süresinin ölçülmesi
start = time.time()
BruteForceSort(arr)
end = time.time()
print("BruteForce çalışma süresi: ", end - start, "saniye")


Öncelikle, rastgele bir 10000 sayı oluşturacağız:

import random

arr = [random.randint(1, 1000) for i in range(10000)]

Daha sonra, birleştirme sıralaması uygulayacağız:

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

sorted_arr = merge_sort(arr)


Sıralama süresi, aşağıdaki gibi ölçülebilir:

import time

start_time = time.time()

sorted_arr = merge_sort(arr)

end_time = time.time()

print("Merge sort time:", end_time - start_time, "seconds")




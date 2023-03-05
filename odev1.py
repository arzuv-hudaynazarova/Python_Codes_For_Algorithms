import time
import random

# Linear Search algoritma:
def linear_search(dizi):
    max_num = dizi[0]
    for i in range(1, len(dizi)):
        if dizi[i] > max_num:
            max_num = dizi[i]
    return max_num


#BruteForce algoritması:
def bruteforce(dizi):
    max_num = dizi[0]
    for i in range(len(dizi)):
        for j in range(len(dizi)):
            if dizi[j] > max_num:
                max_num = dizi[j]
    return max_num

# Rastgele 10000 sayılı bir dizi oluşturalım:
dizi = [random.randint(1, 10000) for i in range(10000)]

#"Linear Search" algoritmasının çalışma süresi:
start_time = time.time()
max_num = linear_search(dizi)
end_time = time.time()
print("En büyük sayı: ", max_num)
print("Linear Search çalışma süresi: ", end_time - start_time,  "saniye")


# BruteForce algoritmasının çalışma süresi:
start_time = time.time()
max_num = bruteforce(dizi)
end_time = time.time()
print("En büyük sayı: ", max_num)
print("BruteForce çalışma süresi: ", end_time - start_time , "saniye")

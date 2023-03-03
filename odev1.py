import time
import random


# Kendi hazırladığım algoritma:
def max_element(dizi):
    max_num = dizi[0]
    for i in range(1, len(dizi)):
        if dizi[i] > max_num:
            max_num = dizi[i]
    return max_num


# Rastgele 10000 sayılı bir dizi oluşturalım en büyük sayıyı gösterme:
dizi = [random.randint(0, 10000) for _ in range(10000)]
print(max_element(dizi))



#BruteForce algoritması:
def max_element_bruteforce(dizi):
    max_num = dizi[0]
    for i in range(len(dizi)):
        for j in range(len(dizi)):
            if dizi[j] > max_num:
                max_num = dizi[j]
    return max_num


# Rastgele 10000 sayılı bir dizi oluşturalım ve ekranda en büyük sayıyı gösterme:
dizi = [random.randint(0, 10000) for _ in range(10000)]
print(max_element_bruteforce(dizi))


# Rastgele 10000 sayılı bir dizi oluşturalım:
dizi = [random.randint(0, 10000) for _ in range(10000)]


#"Linear Search" algoritmasının çalışma süresi:
start_time = time.time()
max_num = max_element(dizi)
end_time = time.time()
print("En büyük sayı: ", max_num)
print("Linear Search çalışma süresi: ", end_time - start_time,  "saniye")


# BruteForce algoritmasının çalışma süresi:
start_time = time.time()
max_num = max_element_bruteforce(dizi)
end_time = time.time()
print("En büyük sayı: ", max_num)
print("BruteForce çalışma süresi: ", end_time - start_time , "saniye")

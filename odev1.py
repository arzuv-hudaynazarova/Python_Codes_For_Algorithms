1.	Bir dizi içindeki en büyük sayıyı en hızlı bulmak için hangi algoritmayı kullanırsınız? 
Önerdiğiniz algoritmayı rastgele oluşturulmuş 10000 sayılık bir dizi üzerinde gerçekleştirin.
Çalışma süresini belirtin. Aynı dizi üzerinde BruteForce bir algoritmanın çalışma süresini hesaplayın ve iki algoritmayı kıyaslayın.
Dilediğiniz bir programlama dilini kullanabilirsiniz. Her iki algoritma için herhangi bir hazır fonkisyon kullanılmamalıdır.
Örnek: Python dilinde max() metodu en büyük elemanı bulmaktadır. Bu tarz hazır fonksiyonlar kesinlikle kabul edilmeyecektir. 
(Kodlar Github üzerinden gönderilmeli.)

# Kendi hazırladığım algoritma:
import time

def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

# Rastgele 10000 sayılı bir dizi oluşturalım
import random
arr = [random.randint(0, 1000) for i in range(10000)]

# "max" algoritmasının çalışma süresi
start_time = time.time()
max_num = find_max(arr)
end_time = time.time()
print("En büyük sayı:", max_num)
print("max algoritmasının çalışma süresi:", end_time - start_time, "saniye")

#BruteForce algoritması:
def brute_force_max(arr):
    n = len(arr)
    max_num = arr[0]
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > max_num:
                max_num = arr[j]
    return max_num

# BruteForce algoritmasının çalışma süresi
start_time = time.time()
max_num = brute_force_max(arr)
end_time = time.time()
print("En büyük sayı:", max_num)
print("BruteForce algoritmasının çalışma süresi:", end_time - start_time, "saniye")


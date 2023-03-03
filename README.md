# Python_Codes_For_Algorithms
Python_Algorithm_design_and_analysis_Lesson


# 1 ödevin açıklama kısmı: 
  Bir dizi içindeki en büyük sayıyı en hızlı bulmak için hangi algoritmayı kullanırsınız? Önerdiğiniz algoritmayı rastgele oluşturulmuş 10000 sayılık bir dizi üzerinde gerçekleştirin. Çalışma süresini belirtin. Aynı dizi üzerinde BruteForce bir algoritmanın çalışma süresini hesaplayın ve iki algoritmayı kıyaslayın. Dilediğiniz bir programlama dilini kullanabilirsiniz. Her iki algoritma için herhangi bir hazır fonkisyon kullanılmamalıdır. Örnek: Python dilinde max() metodu en büyük elemanı bulmaktadır. Bu tarz hazır fonksiyonlar kesinlikle kabul edilmeyecektir. (Kodlar Github üzerinden gönderilmeli.)


En hızlı yöntem, lineer zaman karmaşıklığı olan "Linear Search" olarak da bilinen "Tekrarlayan Kontrol Yöntemi"dir. Bu yöntem, diziyi bir kez tarayarak en büyük elemanı bulur. Bu işlem, n elemanlı bir dizide O(n) zaman karmaşıklığına sahiptir.
Linear Search, verilen bir dizi içinde belirli bir elemanı aramak için kullanılan basit bir arama algoritmasıdır. Bu algoritma, her elemanın sırasıyla kontrol edilerek aranan eleman bulunana kadar arama işlemini sürdürür. Bu nedenle, en kötü durumda tüm dizinin tamamının taranması gerekebilir. Bu algoritmanın karmaşıklığı O(n) 'dir (n dizinin eleman sayısıdır).

Brute Force algoritması ise, tüm olası çözümleri deneyerek sonuca ulaşan bir algoritmadır. Yani, tüm mümkün olası seçenekleri test ederek en iyi sonuca ulaşmaya çalışır. Birçok problem için en kötü durumda çok yavaş çalışabilir. Brute Force algoritmasının karmaşıklığı, çözülen probleme bağlı olarak farklılık gösterir. Ancak, genellikle O(n^2) veya daha kötüsüdür.

En büyük sayıyı bulmak için Linear Search algoritması, her elemanı tek tek kontrol ederek bulur. Bu nedenle, verilen bir dizinin en büyük sayısını bulmak için bu yöntem oldukça hızlıdır. Ancak, Brute Force algoritması tüm olası sayıları tarayarak en büyük sayıyı bulacağından, bu durumda daha yavaş çalışır.


# 2 ödevin açıklama kısmı:
   Veri sıralama işlemi için en iyi algoritma hangisidir ve neden? Önerdiğiniz algoritmayı rastgele oluşturulmuş 10000 sayılık bir dizi üzerinde gerçekleştirin. Çalışma süresini belirtin. Aynı dizi üzerinde BruteForce bir algoritmanın çalışma süresini hesaplayın ve iki algoritmayı kıyaslayın. Dilediğiniz bir programlama dilini kullanabilirsiniz. Her iki algoritma için herhangi bir hazır fonkisyon kullanılmamalıdır. Örnek: Python dilinde sort() metodu sıralama yapamaktadır. Bu tarz hazır fonksiyonlar kesinlikle kabul edilmeyecektir. (Kodlar Github üzerinden gönderilmeli.)

En iyi sıralama algoritması, veri boyutuna bağlı olarak değişebilir. Ancak, genellikle, en iyi performansı sağlamak için hızlı sıralama (quick sort) veya birleştirme sıralaması (merge sort) gibi böl ve yönet algoritmaları tercih edilir.

Hızlı sıralama, bir bölme işlemi ile çalışır. Öncelikle bir anahtar eleman seçilir ve dizinin bu anahtar elemanına göre iki parçaya ayrılması işlemi gerçekleştirilir. Daha sonra, bu iki parçanın her biri için aynı işlem tekrar edilir. Bu işlem, parçaların tek elemanlı hale gelinceye kadar tekrar edilir. Sonunda, tüm parçalar birleştirilir ve sıralı dizi oluşturulur. Hızlı sıralama, en kötü durumda bile O(n log n) karmaşıklığına sahiptir ve pratikte çok hızlı çalışır.

Birleştirme sıralaması, bir dizi parçayı ayrı ayrı sıralar ve daha sonra bu sıralanmış parçaları birleştirir. Bir parçanın sıralanması, parça tek elemanlı hale gelinceye kadar tekrarlanır. Bu yöntem, en kötü durumda bile O(n log n) karmaşıklığına sahiptir ve verimli bir şekilde çalışır.



Burada yapılan işlem, rastgele bir dizi oluşturmak ve bu diziyi üç farklı sıralama algoritması ile sıralamaktır: merge sort, quick sort ve BruteForce sıralama algoritması.

Merge sort, n log n zamanında çalışan ve istikrarlı bir algoritma olarak bilinir. Bu nedenle, 10000 elemanlı bir diziyi sıralamak için oldukça hızlı bir seçenek olarak kabul edilir.

Quick sort, en kötü durumda n^2 zamanında çalışabilen bir algoritmadır. Ancak, ortalama durumda n log n zamanında çalışır ve sıralama işlemini gerçekleştirmek için minimum bellek kullanır.

BruteForce sıralama algoritması, bir diziyi sıralamak için tüm elemanların karşılaştırılması gerektiği n^2 zamanında çalışan bir algoritmadır. Bu nedenle, büyük veri setleri için yavaş bir seçenek olarak kabul edilir.

Yukarıdaki kod parçasında, merge sort ve quick sort algoritmaları örnek olarak gösterilmiş ve her iki algoritma da rastgele oluşturulan 10000 elemanlı bir dizi üzerinde uygulanmıştır. Çalışma süreleri, zaman modülü yardımıyla ölçülmüştür.

Genellikle merge sort'un çalışma süresinin quick sort'a kıyasla daha kısadır. Ayrıca, BruteForce algoritması ile sıralama işleminin oldukça yavaş olduğuda bilinmektedir.

Sonuç olarak, büyük veri setleri için merge sort algoritması tercih edilen bir seçenek olarak kabul edilir. Ancak, veri setinin boyutu küçükse veya bellek kullanımı sınırlıysa, quick sort veya diğer sıralama algoritmaları tercih edilebilir.


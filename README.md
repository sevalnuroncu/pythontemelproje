# pythontemelproje
"""ilk soru:
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]


ikinci soru:
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""



#ilk soruyu önce tek tek mantığını anlamaya çalışrak yapmaya çalıştım. çok fazla for döngüsü kullandım.--->flatten.py
Sonra generatör oluşturarak çözen bir kod buldum ve anlamaya çalıştım.---->flatten2.py
Sonra flatten.py de yazdığım uzun kodun fonksiyon oluşturarak yapılan şeklini buldum. --->flatten3.py  en iyi çözüm buydu bence. Fonksiyon şart sağlanmadıkça kendi kendine döngüye giriyor.

ikinci soruda önce for döngüsü ile liste içindeki listelerin tersi reverse fonk. kullanılarak alındı. Sonrada döngüden çıkıp listenin tersi alınarak soru çözülmüş oldu.



"""
1. continue Komutu
📌 Tanım
continue, döngü içinde bulunduğu anda o iterasyonu (turunu) atlar ve döngünün bir sonraki turuna geçer.
Döngü tamamen durmaz, çalışmaya devam eder.
🧠 Mantık: “Bu durumu görmezden gel ve devam et.”
📌 Kullanım Alanları
    İstenmeyen değerleri atlamak
    Filtreleme yapmak
    Gereksiz işlem yapmamak
"""
# 📌 Örnek 1
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
"""
🔎 Açıklama
i == 2 olduğunda continue çalışır
print(i) satırı atlanır
Döngü bir sonraki değerden devam eder
✅ Çıktı
0
1
3
4
"""
# 📌 Örnek 2 (Filtreleme)
# sayilar = [10, -5, 20, -3, 30]
#
# for sayi in sayilar:
#     if sayi < 0:
#         continue
#     print(sayi)
"""
🔎 Açıklama
Negatif sayılar atlanır
Sadece pozitif sayılar yazdırılır
✅ Çıktı
10
20
30
⚠️ Not
continue, döngüyü bitirmez
Sadece o anki turu atlar
🔹 2. break Komutu
📌 Tanım
break, bulunduğu döngüyü tamamen durdurur ve döngüden çıkar.
🧠 Mantık: “Artık devam etmeye gerek yok, çık.”
📌 Kullanım Alanları
Arama işlemleri (bulunca durmak)
Sonsuz döngüden çıkmak
Belirli bir şartta işlemi kesmek
"""
# 📌 Örnek 1
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
"""
🔎 Açıklama
i == 5 olduğunda döngü tamamen durur
Sonraki değerler çalışmaz
✅ Çıktı
0
1
2
3
4
"""
# 📌 Örnek 2 (Arama işlemi)
# sayilar = [3, 7, 2, 9, 5]
#
# for sayi in sayilar:
#     if sayi == 9:
#         print("Bulundu!")
#         break
"""
🔎 Açıklama
9 bulunduğu anda döngü sonlanır
Gereksiz diğer elemanlara bakılmaz
✅ Çıktı
Bulundu!
"""
# 📌 Örnek 3 (while ile kullanım)
# while True:
#     parola = input("Parola gir: ")
#     if parola == "1234":
#         print("Doğru parola!")
#         break
#     else:
#         print("Yanlış, tekrar dene.")
"""
⚠️ Not
break, döngüyü tamamen bitirir
Döngüden sonra gelen kodlar çalışmaya devam eder
🔑 GENEL KARŞILAŞTIRMA
Özellik	continue	break
Etki	Sadece o turu atlar	Döngüyü tamamen bitirir
Döngü	Devam eder	Sonlanır
Kullanım	Filtreleme	Arama / durdurma
"""

# ------------------------ #


name = "Christopher Bang Chan"

for letter in name:
    print(letter)
"""
    > python break-continue.py
        C
        h
        r
        i
        s
        t
        o
        p
        h
        e
        r
         
        B
        a
        n
        g
         
        C
        h
        n
        a
"""

# ------------------------ #

for letter in name:
    if letter == "a":
        continue
    print(letter)
"""
    > python break-continue.py
        C
        h
        r
        i
        s
        t
        o
        p
        h
        e
        r
         
        B
        n
        g
         
        C
        h
        n
"""

# ------------------------ #

for letter in name:
    if letter == "a":
        break
    print(letter)
"""
    > python break-continue.py
        C
        h
        r
        i
        s
        t
        o
        p
        h
        e
        r
         
        B
"""

# ------------------------ #

i = 0

while i < 8 :
    i += 1
    if i == 2 :
        continue
    print(i)
"""
    > python break-continue.py
        1
        3
        4
        5
        6    
        7
        8
"""

# ------------------------ #

while i < 8 :
    i += 1
    if i == 5 :
        break
    print(i)
"""
    > python break-continue.py
        1
        2   
        3
        4
"""

# ------------------------ #

sum = 0

while i <= 100 :
    i += 1
    if i % 2 == 0 :
        continue
    sum += i

print(sum)
"""
    > python break-continue.py
        2601
"""

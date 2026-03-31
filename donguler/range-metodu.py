"""
range() Metodu
📌 Tanım
range(), belirli bir aralıkta sayılar üretmek için kullanılır.
Genellikle for döngüsü ile birlikte kullanılır.
🧠 Mantık: “Belirli bir sayı aralığında sırayla ilerle.”
📌 Kullanım Şekilleri
1️⃣ Tek parametreli kullanım:
    range(bitis)
👉 0’dan başlar, bitis değerine kadar gider (bitis dahil değildir)
"""
# 📌 Örnek
# for i in range(5):
#     print(i)
# ✅ Çıktı
# 0
# 1
# 2
# 3
# 4
"""
2️⃣ İki parametreli kullanım
range(baslangic, bitis)

👉 baslangic dahil, bitis dahil değildir
"""
# 📌 Örnek
# for i in range(2, 6):
#     print(i)
# ✅ Çıktı
# 2
# 3
# 4
# 5
"""
3️⃣ Üç parametreli kullanım
range(baslangic, bitis, artis)

👉 Belirli adımlarla ilerler
"""
# 📌 Örnek (2’şer artma)
# for i in range(0, 10, 2):
#     print(i)
# ✅ Çıktı+
# 0
# 2
# 4
# 6
# 8

# 📌 Örnek (geri sayma)
# for i in range(10, 0, -1):
#     print(i)
# ✅ Çıktı
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

"""
⚠️ Notlar
    range() sadece tam sayılarla (int) çalışır
    Liste gibi davranır ama aslında hafızada liste tutmaz (performanslıdır)
"""


# ------------------------ #


lists = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(1, 25, 2) :
    """print(i)"""
"""
    > python range-metodu.py
        1
        3
        5
        7
        9
        11
        13
        15
        17
        19
        21
        23
"""

# ------------------------ #

# rng = range(10)

# result = list(rng)
# print(result)
"""
    > python range-metodu.py
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# ------------------------ #

# rng = range(10, 20)
# result = list(rng)
# print(result)
"""
    > python range-metodu.py
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

# ------------------------ #

# rng = range(100, 200, 10)
# result = list(rng)
# print(result)
"""
    > python range-metodu.py
        [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
"""

# ------------------------ #

for i in range (50, 70) :
    if i%2 == 0 :
        print(i)
"""
    > python range-metodu.py
        50
        52
        54
        56
        58
        60
        62
        64
        66
        68
"""
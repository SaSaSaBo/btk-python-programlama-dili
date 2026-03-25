"""
Değişkene değer atamak veya mevcut değeri güncellemek için kullanılır. En temeli = işaretidir.

Python'da işlemleri kısaltmak için pratik yazımlar vardır:
"""
# x = 10
#
# x = x + 5   # Klasik yöntem (x artık 15)
# x += 5      # KISA YOL (x artık 20)
#
# # Diğerleri için de geçerli:
# x -= 2      # x = x - 2 demektir
# x *= 3      # x = x * 3 demektir
# x /= 2      # x = x / 2 demektir


# ------------------------ #

a = 50
b = 30
c = 10

# a, b, c = 50, 30, 10 # şeklinde de yazılabilir
# Her işlemden önceki ve sonraki işlemler yorum satırı yapılmıştır
a += 10

print("1. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    1. Sonuç: a: 60 b: 30 c: 10
"""

b -= 10

print("2. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    2. Sonuç: a: 50 b: 20 c: 10
"""

c *= 8

print("3. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    3. Sonuç: a: 50 b: 30 c: 80
"""

c /= 2

print("4. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    4. Sonuç: a: 50 b: 30 c: 5.0
"""

c %= 3

print("5. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    5. Sonuç: a: 50 b: 30 c: 1
"""

a **= 2

print("6. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    6. Sonuç: a: 2500 b: 30 c: 10
"""

b //= 5

print("7. Sonuç: " "a: " + str(a) + " b: " + str(b) + " c: " + str(c))
# Çıktı:
"""
> python atama-operatorleri.py
    7. Sonuç: a: 50 b: 6 c: 10
"""
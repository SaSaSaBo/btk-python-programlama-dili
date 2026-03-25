"""
Mülakatlarda ve hata ayıklamada en çok lazım olacak konudur.

1. Value Types (Değer Tipleri): int, float, string, bool Verinin kendisi kopyalanır. Birbirinden bağımsızdırlar.
"""
# x = 5
# y = x
# x = 10
# # y hala 5'tir. x'in değişmesi y'yi etkilemez.
"""
2. Reference Types (Referans Tipleri): list, class Verinin kendisi değil, bellekteki adresi kopyalanır. İki değişken aynı listeye bakıyorsa, birinde yapılan değişiklik diğerini de etkiler.
"""
# a = ["muz", "elma"]
# b = a  # DİKKAT: Liste kopyalanmadı, adres eşitlendi.
#
# a[0] = "üzüm"
#
# print(b[0])
# # Çıktı: "üzüm" -> Çünkü b ve a bellekte AYNI kutuya bakıyor.


# ------------------------ #

a = ["elma", "armut"]
b = ["elma", "armut"]
# a = b # adres kopyalandı
a[0] = "üzüm"

print(a, b)
# Çıktı:
"""
> python value-reference.py
    ['üzüm', 'armut'] ['elma', 'armut']
"""

# ------------------------ #

# liste kopyalama
list_a = [10, 20]
list_b = list_a.copy() # 1. yöntem
list_b[0] = 30

print(list_a, list_b)
# Çıktı:
"""
> python value-reference.py
    [10, 20] [30, 20]
"""

list_b = list(list_a)
list_b[0] = 40

print(list_a, list_b)
# Çıktı:
"""
> python value-reference.py
    [10, 20] [40, 20]
"""
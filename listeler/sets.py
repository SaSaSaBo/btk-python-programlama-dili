"""
Matematikteki kümeler gibidir.
Sırasızdır: İndeks numarası yoktur (set[0] diyemezsin).
Eşsizdir (Unique): Aynı elemandan sadece bir tane barındırır. Tekrar eden verileri temizlemek için harikadır.
"""
# meyveler = { "elma", "armut", "elma", "elma" }
# print(meyveler)
# # Çıktı: {'elma', 'armut'} -> Fazla elmalar otomatik silindi.


# ------------------------ #

fruits = {"elma", "armut", "kiraz", "elma"} # set içerisinin tek tip olması zorunlu değil
outcome = fruits

print("Sonuç: " + str(outcome))
# Çıktı:
"""
> python sets.py
    Sonuç: {'elma', 'armut', 'kiraz'}
"""

for x in fruits:
    print("for döngüsü: " + x)
# Çıktı:
"""
> python sets.py
    for döngüsü: elma
    for döngüsü: kiraz
    for döngüsü: armut
"""

# ------------------------ #

outcome_find = "elma" in fruits

print("içerisinde 'elma' değeri var mı: " + str(outcome_find))
# Çıktı:
"""
> python sets.py
    içerisinde 'elma' değeri var mı: True
"""

# ------------------------ #

fruits2 = {"elma", "armut", "kiraz", "kavun"}
fruits.update(fruits2)

print("fruits2'nin eklenmesi: " + str(fruits))
# Çıktı:
"""
> python sets.py
    fruits2'nin eklenmesi: {'kavun', 'armut', 'elma', 'kiraz'}
"""

# ------------------------ #

fruits.add("karpuz")

print("Yeni değer eklenmesi: " + str(fruits))
# Çıktı:
"""
> python sets.py
    Yeni değer eklenmesi: {'elma', 'armut', 'karpuz', 'kavun', 'kiraz'}
"""

# ------------------------ #

fruits.remove("elma")

print("elma değerinin remove silinmesi: " + str(fruits))
# Çıktı:
"""
> python sets.py
    elma değerinin remove silinmesi: {'kavun', 'karpuz', 'armut', 'kiraz'}
"""

# ------------------------ #

fruits.discard("armut")

print("armut değerinin discard ile silinmesi: " + str(fruits))
# Çıktı:
"""
> python sets.py
    armut değerinin discard ile silinmesi: {'kiraz', 'kavun', 'karpuz'}
"""

# ------------------------ #

fruits.pop()

print("pop değeri ile herhangi bir değeri silme: " + str(fruits)) # print çalıştırılmadan önce remove ve discard yorum satırı yapıldı
# Çıktı:
"""
> python sets.py
    pop değeri ile herhangi bir değeri silme: {'karpuz', 'kavun', 'elma', 'kiraz'}
"""
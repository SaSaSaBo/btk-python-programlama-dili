"""
Döngüler, belirlediğimiz kod bloklarının defalarca çalışmasını sağlar.
For Döngüsü: Genellikle elimizde bir veri grubu (liste, string, tuple, dictionary) olduğunda ve "bunun içindeki her bir elemanı tek tek gez" demek istediğimizde kullanırız.
"""
# isimler = ["Ali", "Veli", "Ayşe"]
#
# for isim in isimler:
#     print(isim)
#
# # Çıktı:
# # Ali
# # Veli
# # Ayşe
"""
Burada isim değişkeni her turda listenin sıradaki elemanını temsil eder.
"""

# ------------------------ #

# for -> list
numbers = [8, 1, 19, 3, 25, 18]
names = ["bangchan", "leeknow", "changbin", "hyunjin", "han", "felix", "seungmin", "i.n"]

for x in numbers:
    print("for döngüsü sonucu: " + str(x))
# Çıktı:
"""
> python python for.py
    for döngüsü sonucu: 8
    for döngüsü sonucu: 1
    for döngüsü sonucu: 19
    for döngüsü sonucu: 3
    for döngüsü sonucu: 25
    for döngüsü sonucu: 18
"""

# ------------------------ #

for x in names:
    print("StrayKids üyesi: " + str(x))
# Çıktı:
"""
> python python for.py
    StrayKids üyesi: bangchan
    StrayKids üyesi: leeknow
    StrayKids üyesi: changbin
    StrayKids üyesi: hyunjin
    StrayKids üyesi: han
    StrayKids üyesi: felix
    StrayKids üyesi: seungmin
    StrayKids üyesi: i.n
"""

# ------------------------ #

for name in names:
    print("StrayKids: " + str(name))
# Çıktı:
"""
> python python for.py
    StrayKids: bangchan
    StrayKids: leeknow
    StrayKids: changbin
    StrayKids: hyunjin
    StrayKids: han
    StrayKids: felix
    StrayKids: seungmin
    StrayKids: i.n
"""

# ------------------------ #

nick_name = "stay"

for i in nick_name:
    print("You make StrayKids: " + str(i))
# Çıktı:
"""
> python python for.py
    You make StrayKids: s
    You make StrayKids: t
    You make StrayKids: a
    You make StrayKids: y
"""

# ------------------------ #

my_tuple = [(3, 25), (3, 18), (8, 19), (8, 1)]

for i in my_tuple:
    print("dates: " + str(i))
# Çıktı:
"""
> python python for.py
    dates: (3, 25)
    dates: (3, 18)
    dates: (8, 19)
    dates: (8, 1)
"""

# ------------------------ #

for (a, b) in my_tuple:
    print("dates one by one: " + str(a), str(b))
# Çıktı:
"""
> python python for.py
    dates one by one: 3 25
    dates one by one: 3 18
    dates one by one: 8 19
    dates one by one: 8 1
"""

# ------------------------ #

my_dict = {"41": "Kocaeli", "34": "İstanbul", "5": "Amasya", "6": "Ankara"}

for x in my_dict: # my_dict.values() -> illeri verir # my_dict.keys() -> plakaları verir # (x, y) in my_dict.items() -> iller ve plakaları bir arada verir
    print("plakalar: " + str(x))
    print("İller: " + str(my_dict[x]))
# Çıktı:
"""
> python python for.py
    plakalar: 41
    İller: Kocaeli
    plakalar: 34
    İller: İstanbul
    plakalar: 5
    İller: Amasya
    plakalar: 6
    İller: Ankara
"""
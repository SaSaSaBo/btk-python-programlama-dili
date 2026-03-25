"""
Python'a özgü, kodu İngilizce cümle gibi okumamızı sağlayan harika operatörlerdir.
A. Identity (Kimlik) Operatörü: is
Bu operatör değerlerin eşitliğine (==) bakmaz, bellekteki adreslerinin aynı olup olmadığına bakar. (Hatırla: Value vs Reference Types konusu).
"""
# x = [1, 2, 3]
# y = [1, 2, 3]
#
# print(x == y)  # True (Çünkü içindeki değerler aynı)
# print(x is y)  # False (Çünkü bunlar bellekte farklı kutular/objeler)
#
# z = x
# print(x is z)  # True (Çünkü z, x'in adresini tutuyor)
"""
B. Membership (Üyelik) Operatörü: in
Bir listenin veya metnin içinde aradığımız değerin olup olmadığını sorar.
"""
# # Listelerde
# isimler = ["ali", "veli"]
# print("ali" in isimler)  # True (Listede var mı? Evet)
#
# # Stringlerde
# ad = "Sadık Turan"
# print("a" in ad)         # True (Metnin içinde 'a' harfi geçiyor mu?)
# print("x" not in ad)     # True ('x' harfi YOK değil mi? Evet yok.)


# ------------------------ #

# identity
x = [2, 4, 6]
y = [2, 4, 6]
z = y

print("x, y'ye eşit midir: " + str(x == y))
print("x, y midir: " + str(x is y))
print("x, y değil midir: " + str(x is not y))
print("z, y midir: " + str(z is y))
print("z, y değil midir: " + str(z is not y))
# Çıktı:
"""
> python identity-ve-membership-operatorleri.py
    x, y'ye eşit midir: True
    x, y midir: False
    x, y değil midir: True
    z, y midir: True
    z, y değil midir: False
"""

# ------------------------ #

# membership
print("20, x'de elemanı mıdır: " + str(20 in x))
print("20, x'de elemanı değil midir: " + str(20 not in x))
# Çıktı:
"""
> python identity-ve-membership-operatorleri.py
    20, x'de elemanı mıdır: False
    20, x'de elemanı değil midir: True
"""
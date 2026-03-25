"""
Uygulama 1 : Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
Alan: πr²
Çevre: 2πr

Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
mil = km / 1.609344
"""

# 1. Uygulama:
pi = 3.14
r = float(input("Yarı Çap: "))

area = pi * (r ** 2)
circle = 2 * pi * r

print("Alan: " + str(area))
print("Çevre: " + str(circle))

# Çıktı:
"""
> python uygulama-veri-tipleri.py
    Yarı Çap: 8
    Alan: 200.96
    Çevre: 50.24
"""

# ------------------------ #

# 2. Uygulama:
mil= 1.609344
distance_km = input("km: ")
distance_mile = float(distance_km) / mil
# distance_mile = round(distance_mile, 2) -> Çıktı o zaman "Mil Cinsinden değeri: 497.8"
print("Girilen km değeri: " + distance_km)
print("Mil Cinsinden değeri: " + str(distance_mile))

# Çıktı:
"""
> python uygulama-veri-tipleri.py
    km: 801
    Girilen km değeri: 801
    Mil Cinsinden değeri: 497.7183249821045
"""
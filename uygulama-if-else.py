"""
1. Bir aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
benzin : 39.35
dizel : 41.71
lpg : 20.28

2. Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.
0 - 24 -> 0
25 - 44 -> 1
45 - 54 -> 2
55 - 69 -> 3
70 - 84 -> 4
85 - 100 -> 5
"""

# 1. Soru:
gas_cost = 39.35
diesel_cost = 41.71
lpg_cost = 20.28

average_fuel_consumption = float(input("100km'deki ortalama yakıt tüketimi: "))
to_go = float(input("Gidilen mesafe: "))
fuel_type = input("Yakıt tipi: ")

total_fuel_consumption = to_go * (average_fuel_consumption / 100)
total_fuel_cost = 0

if fuel_type == "benzin":
    total_fuel_cost = gas_cost * total_fuel_consumption
    print("Toplam benzin ücreti: ", total_fuel_cost)
elif fuel_type == "dizel":
    total_fuel_cost = diesel_cost * total_fuel_consumption
    print("Toplam dizel ücreti: ", total_fuel_cost)
elif fuel_type == "lpg":
    total_fuel_cost = lpg_cost * total_fuel_consumption
    print("Toplam lpg ücreti: ", total_fuel_cost)
else :
    print("Girilen değerlerle ilgili veri bulunamamadığından işlem yapılamıyor.")
# Çıktı:
"""
> python uygulama-if-else.py
    100km'deki ortalama yakıt tüketimi: 7.2
    Gidilen mesafe: 50
    Yakıt tipi: benzin
    Toplam benzin ücreti:  141.66000000000003
    # ------------------------ #
    100km'deki ortalama yakıt tüketimi: 5.8
    Gidilen mesafe: 100
    Yakıt tipi: dizel
    Toplam dizel ücreti:  241.918
    # ------------------------ #
    100km'deki ortalama yakıt tüketimi: 6.4
    Gidilen mesafe: 65
    Yakıt tipi: lpg
    Toplam lpg ücreti:  84.3648
"""

print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
exam1 = float(input("1. Sınav Notu:"))
exam2 = float(input("2. Sınav Notu:"))
quiz = float(input("Quiz Notu: "))

average = (exam1 + exam2 + quiz) / 3

if (average >= 0) and (average < 25):
    print(f"Ortalama: {average} ve değerlendirme notu: 0")
elif (average >= 25) and (average < 45):
    print(f"Ortalama: {average} ve değerlendirme notu: 1")
elif (average >= 45) and (average < 55):
    print(f"Ortalama: {average} ve değerlendirme notu: 2")
elif (average >= 55) and (average < 70):
    print(f"Ortalama: {average} ve değerlendirme notu: 3")
elif (average >= 70) and (average < 85):
    print(f"Ortalama: {average} ve değerlendirme notu: 4")
elif (average >= 85) and (average < 100):
    print(f"Ortalama: {average} ve değerlendirme notu: 5")
else :
    pass
# Çıktı:
"""
> python uygulama-if-else.py
    1. Sınav Notu:60
    2. Sınav Notu:40
    Quiz Notu: 70
    Ortalama: 56.666666666666664 ve değerlendirme notu: 3
"""
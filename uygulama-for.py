"""
1. "numbers" listesindeki her bir elemanı yazdırınız.
2. "numbers" listesinde hangi sayılar 3'ün katıdır?
3. "numbers" listesinde tüm satıların toplamı nedir?
4. "products" listesindeki tüm iphone marka ürünleri listeleyiniz.
5. "products" listesinde kaç adet samsung ürünü vardır?
6. Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
    "HP Victus marka ürünün fiyatı 32999 TL'dir."
7. Ürünlerin fiyatları toplamı nedir?
8. 25000 ile 40000 arasındaki ürünleri listeleyiniz.
9. Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.
"""

numbers = [3, 25, 18, 8, 1, 19, 26]
products = ["samsung s25", "samsung s24", "iphone 16", "iphone 17"]
brands = [
    {
        "brand_name": "HP Victus",
        "cost": 32999
    },
    {
        "brand_name": "Lenovo ThinkPad",
        "cost": 25499
    },
    {
        "brand_name": "Apple Macbook",
        "cost": 49999
    },
    {
        "brand_name": "Huawei Matebook",
        "cost": 26999
    },
    {
        "brand_name": "Casper Nirvana",
        "cost": 20000
    }
]

# 1. Soru:
for number in numbers :
    print("Sayı bilgisi: " + str(number))
# Çıktı:
"""
> python uygulama-for.py
    Sayı bilgisi: 3
    Sayı bilgisi: 25
    Sayı bilgisi: 18
    Sayı bilgisi: 8
    Sayı bilgisi: 1
    Sayı bilgisi: 19
    Sayı bilgisi: 26
"""

print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
for x in numbers :
    if x % 3 == 0 :
        print("3'ün katı olan sayılar: " + str(x))
# Çıktı:
"""
> python uygulama-for.py
    3'ün katı olan sayılar: 3
    3'ün katı olan sayılar: 18
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
total = 0
for y in numbers :
    total += y
print("Toplam: " + str(total))
# Çıktı:
"""
> python uygulama-for.py
    Toplam: 100
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
for brand in products:
    if "iphone" in brand:
        print("Bulunan iphone ürünleri: " + brand)
# Çıktı:
"""
> python uygulama-for.py
    Bulunan iphone ürünleri: iphone 16
    Bulunan iphone ürünleri: iphone 17
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
counter = 0
for samsung in products :
    index = samsung.find("samsung")
    if index != -1 :
        counter += 1
print("Toplam samsun ürün sayısı: " + str(counter))
# Çıktı:
"""
> python uygulama-for.py
    Toplam samsun ürün sayısı: 2
"""

print("# ------------------------ #")
# ------------------------ #

# 6. Soru:
for laptop in brands :
    print(f"{laptop['brand_name']} marka ürünün fiyatı {laptop["cost"]} TL'dir.")
# Çıktı:
"""
> python uygulama-for.py
    HP Victus marka ürünün fiyatı 32999 TL'dir.
    Lenovo ThinkPad marka ürünün fiyatı 25499 TL'dir.
    Apple Macbook marka ürünün fiyatı 49999 TL'dir.
    Huawei Matebook marka ürünün fiyatı 26999 TL'dir.
    Casper Nirvana marka ürünün fiyatı 20000 TL'dir.
"""

print("# ------------------------ #")
# ------------------------ #

# 7. Soru:
total_cost = 0
for cost in brands :
    total_cost += cost["cost"]
print("Ürünlerin fiyat toplamı: " + str(total_cost))
# Çıktı:
"""
> python uygulama-for.py
    Ürünlerin fiyat toplamı: 155496
"""

print("# ------------------------ #")
# ------------------------ #

# 8. Soru:
for average_cost in brands :
    if (average_cost["cost"] >= 25000) and (average_cost["cost"] <= 40000) :
        print(f"{average_cost["brand_name"]} ortalama fiyata sahiptir.")
# Çıktı:
"""
> python uygulama-for.py
    HP Victus ortalama fiyata sahiptir.
    Lenovo ThinkPad ortalama fiyata sahiptir.
    Huawei Matebook ortalama fiyata sahiptir.
"""

print("# ------------------------ #")
# ------------------------ #

# 9. Soru:
search = input("Aranacak ürün: ")

for search_word in brands :
    if search_word["brand_name"].lower().find(search.lower()) > -1 :
        print(f"Aranan ürün: {search_word['brand_name']} fiyatı {search_word['cost']} TL'dir.")
# Çıktı:
"""
> python uygulama-for.py
    Aranacak ürün: hp
    Aranan ürün: HP Victus fiyatı 32999 TL'dir.
"""
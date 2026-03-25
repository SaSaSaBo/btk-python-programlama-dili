"""
Listelerdeki gibi 0, 1, 2 diye indeks numarası yoktur. Anahtar - Değer (Key - Value) ilişkisi vardır. Gerçek hayattaki sözlükler gibidir (Kelime -> Anlamı).

Tanımlama: Süslü parantez {} kullanılır.
"""
# # plaka kodları örneği
# plakalar = { "kocaeli": 41, "istanbul": 34 }
#
# # Veriye erişim (Key ile çağrılır)
# print(plakalar["kocaeli"])  # Çıktı: 41


# ------------------------ #

cities = ["kocaeli", "istanbul"]
license_plate = [41, 34]

print("Plaka - İl: " + str(license_plate[0]) + " - " + cities[0])
print("Plaka - İl: " + str(license_plate[1]) + " - " + cities[1])
# Çıktı:
"""
> python dictionary.py
    Plaka - İl: 41 - kocaeli
    Plaka - İl: 34 - istanbul
"""

print("index: kocaeli, plaka: " + str(license_plate[cities.index("kocaeli")]))
print("index: istanbul, plaka: " + str(license_plate[cities.index("istanbul")]))
# Çıktı:
"""
> python dictionary.py
    index: kocaeli, plaka: 41
    index: istanbul, plaka: 34
"""

# ------------------------ #

# dictionary
license_plates = {"kocaeli": 41, "istanbul": 34}

print("dictionary - kocaeli: " + str(license_plates["kocaeli"]))
print("dictionary - istanbul: " + str(license_plates["istanbul"]))
# Çıktı:
"""
> python dictionary.py
    dictionary - kocaeli: 41
    dictionary - istanbul: 34
"""

# ------------------------ #

license_plates["izmir"] = 36

print("dictionary - izmir: " + str(license_plates["izmir"]))
# Çıktı:
"""
> python dictionary.py
    dictionary - izmir: 36
"""

# ------------------------ #

license_plate_dictionary = {"kocaeli": 41, "istanbul": 34, "izmir": 35}
# license_plate_dictionary["izmir"] = 35

print("dictionary - izmir: " + str(license_plate_dictionary["izmir"]))
# Çıktı:
"""
> python dictionary.py
    dictionary - izmir: 35
"""
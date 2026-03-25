"""
Listeler üzerinde işlem yapmak için kullanılan hazır fonksiyonlardır. Orijinal listeyi kalıcı olarak değiştirirler.
Metot          |                                Ne Yapar?                                  |           Örnek
.append()      |                     Listenin en sonuna eleman ekler.                      |    liste.append("Yeni")
.insert()      |                     Belirtilen indekse eleman ekler.                      |    liste.insert(0, "Başa")
.pop()         |     Son elemanı (veya belirtilen indeksi) siler ve size geri döndürür.    |        liste.pop()
.remove()      |     Değere göre silme yapar (İlk bulduğunu siler).                        |   liste.remove("Ali")
.sort()        |     Küçükten büyüğe (veya a-z) sıralar.                                   |    sayilar.sort()
.reverse()     |    Listeyi olduğu gibi tersten yazar (sıralama yapmaz, takla attırır).    |    liste.reverse()
.count()       |         Bir elemanın listede kaç tane olduğunu sayar.                     |     liste.count(5)
.clear()       |                      Listeyi tamamen boşaltır.                            |     liste.clear()
"""


# ------------------------ #

numbers = [3, 67, 4, 7, 2, 56, 23, 76]
names = ["Chan", "Minho", "Changbin", "Hyunjin", "Han", "Felix", "Seungmin", "Jeongin" ]

outcome_numbers_min = min(numbers)
outcome_names_min = min(names)
outcome_numbers_max = max(numbers)
outcome_names_max = max(names)

print("Minimum sayı: " + str(outcome_numbers_min))
print("İlk isim: " + str(outcome_names_min))
print("Maximum sayı: " + str(outcome_numbers_max))
print("Son isim: " + str(outcome_names_max))
# Çıktı:
"""
> python uygulama-listeler.py 
    Minimum sayı: 2
    İlk isim: Chan
    Maximum sayı: 76
    Son isim: Seungmin
"""

print("# ------------------------ #")
# ------------------------ #

# ekleme
add_number = numbers.append(12)
add_name = names.append("Stay")

insert_numbers = (0, 100) # > python uygulama-listeler.py > [100, 3, 67, 4, 7, 2, 56, 23, 76, 12]
insert_numbers_end = (-1, 100) # > python uygulama-listeler.py > [3, 67, 4, 7, 2, 56, 23, 76, 100, 12]

print("Sayı ekleme: " + str(numbers))
print("İsim ekleme: " + str(names))
# Çıktı:
"""
> python uygulama-listeler.py 
    Sayı ekleme: [3, 67, 4, 7, 2, 56, 23, 76, 12]
    İsim ekleme: ['Chan', 'Minho', 'Changbin', 'Hyunjin', 'Han', 'Felix', 'Seungmin', 'Jeongin', 'Stay']
"""

print("# ------------------------ #")
# ------------------------ #

# silme
delete_number = numbers.pop()
delete_number_zero = numbers.pop(0)
names.remove("Stay")

print("delete_number: " + str(numbers))
print("delete_number_zero: " + str(numbers))
print("delete_name: " + str(names))
# Çıktı:
"""
> python uygulama-listeler.py 
    delete_number: [3, 67, 4, 7, 2, 56, 23, 76
    delete_number_zero: [67, 4, 7, 2, 56, 23, 76, 12]
    delete_name: ['Chan', 'Minho', 'Changbin', 'Hyunjin', 'Han', 'Felix', 'Seungmin', 'Jeongin']
"""

print("# ------------------------ #")
# ------------------------ #

# sıralama
numbers.sort()
names.sort()

numbers.reverse()
names.reverse()

print("ordering_numbers: " + str(numbers))
print("ordering_names: " + str(names))
print("reverse_numbers: " + str(numbers))
print("reverse_names: " + str(names))
# Çıktı:
"""
> python uygulama-listeler.py 
    ordering_numbers: [2, 4, 7, 23, 56, 67, 76]
    ordering_names: ['Chan', 'Changbin', 'Felix', 'Han', 'Hyunjin', 'Jeongin', 'Minho', 'Seungmin']
    reverse_numbers: [76, 67, 56, 23, 7, 4, 2]
    reverse_names: ['Seungmin', 'Minho', 'Jeongin', 'Hyunjin', 'Han', 'Felix', 'Changbin', 'Chan']
"""

print("# ------------------------ #")
# ------------------------ #

# saydırma
counting_numbers = numbers.count(7)
counting_names = names.count('Seungmin')

print("counting_numbers: " + str(counting_numbers))
print("counting_names: " + str(counting_names))
# Çıktı:
"""
> python uygulama-listeler.py 
    counting_numbers: 1
    counting_names: 1
"""

print("# ------------------------ #")
# ------------------------ #

# arama
search_number = numbers.index(7)
search_names = names.index('Seungmin')

print("search_number: " + str(search_number))
print("search_names: " + str(search_names))
# Çıktı:
"""
> python uygulama-listeler.py 
    search_number: 3
    search_names: 6
"""
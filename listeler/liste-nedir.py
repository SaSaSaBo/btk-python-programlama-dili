"""
Değişkenlerde tek bir veri tutabiliyorduk. Listeler ise birden fazla veriyi tek bir isim altında toplamamızı sağlar.

Özellikleri: Sıralıdır (index numarası vardır), değiştirilebilir (mutable), farklı veri tiplerini bir arada tutabilir.

Tanımlama: Köşeli parantez [] kullanılır.
"""
# # Liste Tanımlama
# sayilar = [1, 2, 3]
# isimler = ["Ali", "Veli", "Ayşe"]
# karisik = [1, "Ali", 3.14, True] # Farklı türler bir arada olabilir
#
# # Erişme (Indexing) - Stringler ile aynı mantık
# print(isimler[0])  # Çıktı: Ali


# ------------------------ #

establishment = "BTK AKADEMİ".split() # str to list

print("establishment type: " + str(type(establishment)))
print("establishment: " + str(establishment))
print("establishment [0]: " + str(establishment[0]))
print("establishment [1]: " + str(establishment[1]))
# Çıktı:
"""
> python liste-nedir.py            
    establishment type: <class 'list'>
    establishment: ['BTK', 'AKADEMİ']
    establishment [0]: BTK
    establishment [1]: AKADEMİ
"""

# ------------------------ #

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
names = ["bangchan", "leeknow", "changbin", "hyunjin", "han", "felix", "seungmin", "jeongin"]

print("numbers type: " + str(type(numbers)))
print("numbers type [0]: " + str(type(numbers[0])))

print("names type: " + str(type(names)))
print("names type [0]: " + str(type(names[0])))
# Çıktı:
"""
> python liste-nedir.py  
    numbers type: <class 'list'>
    numbers type [0]: <class 'int'>
    names type: <class 'list'>
    names type [0]: <class 'str'>
"""

# ------------------------ #

student = ["Cafer", "Bilinmiyor", 60, 50, 70]
average = (student[2] + student[3] + student[4]) / 3

print("student name: " + str(student[0]) + " " + str(student[1]))
print("student average: " + str(average))
# Çıktı:
"""
> python liste-nedir.py  
    student name: Cafer Bilinmiyor
    student average: 60.0
"""

# ------------------------ #

students = [["Ali", "Bilinmiyor", 60, 50, 70], ["Cafer", "Gözlerinin Rengi Bilinmiyor", 30, 25, 40]]

print("first student: " + students[0][0])
print("second student: " + students[1][0])
# Çıktı:
"""
> python liste-nedir.py  
    first student: Ali
    second student: Cafer
"""

# 1. Yol:

# --- 1. Öğrenci (Ali) ---
# students[0] bize Ali'nin listesini verir: ["Ali", "Bilinmiyor", 60, 50, 70]
ali_notlar = students[0]
ali_ortalama = (ali_notlar[2] + ali_notlar[3] + ali_notlar[4]) / 3

print(f"{ali_notlar[0]} isimli öğrencinin ortalaması: {ali_ortalama}")

# --- 2. Öğrenci (Cafer) ---
# students[1] bize Cafer'in listesini verir
cafer_notlar = students[1]
cafer_ortalama = (cafer_notlar[2] + cafer_notlar[3] + cafer_notlar[4]) / 3

print(f"{cafer_notlar[0]} isimli öğrencinin ortalaması: {cafer_ortalama}")
# Çıktı:
"""
> python liste-nedir.py  
    Ali isimli öğrencinin ortalaması: 60.0
    Cafer isimli öğrencinin ortalaması: 31.666666666666668
"""

# 2. Yol:

for ogrenci in students:
    # Bu kod her öğrenci için bir kez çalışır
    ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3
    print(f"{ogrenci[0]} Ortalaması: {ortalama}")
# Çıktı:
"""
> python liste-nedir.py  
    Ali Ortalaması: 60.0
    Cafer Ortalaması: 31.666666666666668
"""
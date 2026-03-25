"""
1. 'title' değişkeni içerisindeki karakter sayısı nedir?
2. 'title' içerisindeki 'Python' kelimesini alın.
3. 'title' değişkenşinin ilk 5 ve son beş karakterini alın.
4. 'title' değişkenini tersten yazdırınız.
5. Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
    Örnek: Cafer Bilinmiyor isimli öğrencinin 1. notu 60, 2. notu 60 ve not ortalaması 60 olarak hesaplanmıştır.
"""

title = "Python ile Programlama Dersleri"

# 1. Soru:
quantity = len(title)
print(quantity)
# Çıktı:
"""
> python uygulama-strings.py
    31
"""

# ------------------------ #

# 2. Soru:
print(title[:6])
# Çıktı:
"""
> python uygulama-strings.py
    Python
"""

# ------------------------ #

# 3. Soru:
print(title[:6])
print(title[-5:])
# Çıktı:
"""
> python uygulama-strings.py
    Python
    sleri
"""

# ------------------------ #

# 4. Soru:
print(title[::-1])
# Çıktı:
"""
> python uygulama-strings.py
    irelsreD amalmargorP eli nohtyP
"""

# ------------------------ #

# 5. Soru:
name = "Cafer"
surname = "Bilinmiyor"
grade1 = grade2 = 60
grade_average = (float(grade1) + float(grade2)) / 2

outcome = f"{name} {surname} isimli öğrencinin 1. notu {grade1}, 2. notu {grade2} ve not ortalaması {grade_average} olarak hesaplanmıştır."
print(outcome)
# Çıktı:
"""
> python uygulama-strings.py
    Cafer Bilinmiyor isimli öğrencinin 1. notu 60, 2. notu 60 ve not ortalaması 60.0 olarak hesaplanmıştır.
"""

name = input("ad: ")
surname = input("soyad: ")
grade1 = input("1. not: ")
grade2 = input("2. not: ")
grade_average = (float(grade1) + float(grade2)) / 2

outcome = f"{name} {surname} isimli öğrencinin 1. notu {grade1}, 2. notu {grade2} ve not ortalaması {grade_average} olarak hesaplanmıştır."
print(outcome)
# Çıktı:
"""
> python uygulama-strings.py
    ad: Minho
    soyad: Lee
    1. not: 85
    2. not: 20
    Minho Lee isimli öğrencinin 1. notu 85, 2. notu 20 ve not ortalaması 52.5 olarak hesaplanmıştır.
"""
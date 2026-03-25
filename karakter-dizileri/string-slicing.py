"""
Bir metnin içinden belirli bir parçayı çekip almaktır. Python'da indeksler 0'dan başlar.

Kalıp: degisken[baslangic : bitis : adim_sayisi]

Tek Karakter Alma: text[0] ilk harfi verir.

Aralık Alma: text[2:5] -> 2. indeksten başlar, 5. indekse kadar alır (5 dahil değildir!).

Baştan/Sondan Gitme:
text[:10] -> En baştan 10'a kadar.
text[5:] -> 5'ten en sona kadar.

Negatif İndeks: Sondan saymak içindir. -1 son karakterdir. text[-5:] sondaki 5 karakteri alır.

Adım (Step): text[::2] baştan sona ikişer ikişer atlayarak alır. text[::-1] metni tersten yazar.
"""


# ------------------------ #

course = "Python ile Programlama"

print(course[0]) # Çıktı: > python string-slicing.py > P
print(course[-1]) # Çıktı: > python string-slicing.py > a

quantity = len(course)

print(quantity) # Çıktı: > python string-slicing.py > 22
# print(course[quantity])
# Çıktı:
"""
> python string-slicing.py
    Traceback (most recent call last):
        File "/string-slicing.py", line 30, in <module>
        print(course[quantity])
              ~~~~~~^^^^^^^^^^
    IndexError: string index out of range
"""
print(course[quantity - 1]) # Çıktı: > python string-slicing.py > a
print(course[0:5]) # Çıktı: > python string-slicing.py > Pytho
print(course[:6]) # Çıktı: > python string-slicing.py > Python
print(course[11:20]) # Çıktı: > python string-slicing.py > Programla
print(course[11:quantity]) # Çıktı: > python string-slicing.py > Programlama
print(course[5:]) # Çıktı: > python string-slicing.py > n ile Programlama
print(course[11:]) # Çıktı: > python string-slicing.py > Programlama
print(course[-11:-1]) # Çıktı: > python string-slicing.py > Programlam
print(course[0:20:2]) # Çıktı: > python string-slicing.py > Pto l rgal
print(course[::]) # Çıktı: > python string-slicing.py > Python ile Programlama
print(course[::2]) # Çıktı: > python string-slicing.py > Pto l rgalm
print(course[::-1]) # Çıktı: > python string-slicing.py > amalmargorP eli nohtyP
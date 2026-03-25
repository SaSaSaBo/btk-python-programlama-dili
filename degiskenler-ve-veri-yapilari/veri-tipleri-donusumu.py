"""
Burası en çok hata yapılan yerlerden biridir. Farklı türdeki verilerle doğrudan işlem yapamazsınız.
"""
# Sorun:
# sayi1 = "10"   # Bu bir String (Metin)
# sayi2 = 20     # Bu bir Integer (Sayı)

# print(sayi1 + sayi2)
# HATA! Python metin ile sayıyı toplayamaz.
"""
Çözüm: Dönüşüm fonksiyonlarını kullanmak.
1. int() - Tam Sayıya Çevirme
Metin halindeki sayıları veya ondalıklı sayıları tam sayıya çevirir.
int("25") -> 25 (Artık matematiksel işlem yapılabilir)
int(10.9) -> 10 (Yuvarlama yapmaz, virgülden sonrasını siler atar).

2. float() - Ondalıklı Sayıya Çevirme
Tam sayıları veya metin halindeki kesirli sayıları ondalıklıya çevirir.
float(12) -> 12.0
float("3.14") -> 3.14

3. str() - Metne Çevirme
Sayıları metne çevirir. Genellikle ekrana yazı yazdırırken sayıları cümlenin içine katmak için kullanılır.
str(99) -> "99"

Örnek Senaryo: Kullanıcıdan Veri Alma:
Bu konunun en önemli kullanım alanı input() fonksiyonudur. Unutma: input() ile kullanıcıdan alınan her şey (sayı girse bile) String (metin) olarak gelir.
"""
# Örnek
# Kullanıcı "1990" girsin
# dogum_yili = input("Doğum yılınız: ")
# dogum_yili şu an "1990" (String)
# Matematiksel işlem yapmak için int'e çevirmeliyiz:
# yas = 2024 - int(dogum_yili)
# print("Yaşınız: " + str(yas))
# yas integer olduğu için string ile birleştirmek adına str() içine aldık.
"""
Özet Tablo
  Fonksiyon  |       Ne Yapar?           |   Örnek Girdi      |        Sonuç
int()        |  Tam sayıya çevirir       |   "50" veya 50.9"  |         50
float()      | Ondalıklı sayıya çevirir  |   "10 veya "10.5"  |    10.0 veya 10.5
str()        | Metne (yazıya) çevirir    |        100         |       "100"
type()       |     Türünü söyler         |        True        |     <class 'bool'>
"""


# ------------------------ #

number1 = input("sayı 1: ")
number2 = input("sayı 2: ")
# input'tan gelen değerler her zaman string değerinde olur

total = number1 + number2

print(total)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    sayı 1: 8
    sayı 2: 01
    801
"""

# ------------------------ #

number3 = int(input("sayı 3: "))
number4 = int(input("sayı 4: "))

total = number3 + number4

print(total)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    sayı 3: 5
    sayı 4: 3
    8
"""

# ------------------------ #

x = int("8")
print(x)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    8
"""

# ------------------------ #

x = int("8.01")
print(x)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    Traceback (most recent call last): File "/veri-tipleri-donusumu.py", line 95, in <module>
    x = int("8.01")
    ValueError: invalid literal for int() with base 10: '8.01'
"""

# ------------------------ #

x = int(8.01)
print(x)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    8
"""

# ------------------------ #

x = float("8")
print(x)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    8.0
"""

# ------------------------ #

x = float("8.01")
print(x)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    8.01
"""

# ------------------------ #

x = str("8.01") # -> str(8.01)
print(x)

# Çıktı:
"""
> python veri-tipleri-donusumu.py
    8.01
"""
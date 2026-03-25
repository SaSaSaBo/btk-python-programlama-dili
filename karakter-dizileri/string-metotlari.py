"""
Stringler birer sınıf (class) olduğu için, kendilerine ait fonksiyonları (metotları) vardır. En sık kullanılanlar:
# --------------------------------------------------------------------------------------------------------------- #
      Metot      |                 Ne Yapar?                 |            Örnek            |       Sonuç
.upper()         |          Hepsini BÜYÜK harf yapar         |         ali.upper()         |       "ALI"
.lower()         |          Hepsini küçük harf yapar         |         ALI.lower()         |       "ali"
.title()         |     Her kelimenin baş harfini büyütür     |      ali veli.title()       |     "Ali Veli"
.capitalize()    |    Sadece cümlenin ilk harfini büyütür    |    ali veli.capitalize()    |     "Ali veli"
.strip()         |    Baştaki ve sondaki boşlukları siler    |    " veri ".strip()         |       "veri"
.split()         |    Metni parçalayıp liste yapar           |   "Ali,Veli".split(",")     |   ['Ali', 'Veli']
.replace()       |           Metin değiştirir                |    çilek.replace("ç","c")   |       "cilek"
.find()          |    Aranan kelimenin kaçıncı indekste      |             -                |          -
                       olduğunu söyler (Yoksa -1 döner)
# --------------------------------------------------------------------------------------------------------------- #
Önemli Not: String metotları orijinal değişkeni değiştirmez, yeni bir veri üretir.
"""
# isim = "ali"
# isim.upper() # Ekrana "ALI" yazar ama 'isim' hala "ali"dir.
# isim = isim.upper() # Şimdi 'isim' kalıcı olarak "ALI" oldu.


# ------------------------ #

message = "BTK akademi, python kursu ders notları"
outcome_upper = message.upper()
# Çıktı:
"""
> python string-metotlari.py
    BTK AKADEMI PYTHON KURSU DERS NOTLARI
"""

# ------------------------ #

outcome_lower = message.lower()
# Çıktı:
"""
> python string-metotlari.py
    btk akademi python kursu ders notları
"""

# ------------------------ #

outcome_title = message.title()
# Çıktı:
"""
> python string-metotlari.py
    Btk Akademi Python Kursu Ders Notları
"""

# ------------------------ #

outcome_capitalize = message.capitalize()
# Çıktı:
"""
> python string-metotlari.py
    Btk akademi python kursu ders notları
"""

# ------------------------ #

outcome_isupper = "skz".isupper()
# Çıktı:
"""
> python string-metotlari.py
    False
"""

# ------------------------ #

outcome_islower = "skz".islower()
# Çıktı:
"""
> python string-metotlari.py
    True
"""

# ------------------------ #

outcome_strip = message.strip()
# Çıktı:
"""
> python string-metotlari.py
    BTK akademi python kursu ders notları
"""

# ------------------------ #

outcome_split = message.split()
# Çıktı:
"""
> python string-metotlari.py
    ['BTK', 'akademi', 'python', 'kursu', 'ders', 'notları']
"""

# ------------------------ #

outcome_split_with_value = message.split(",")
# Çıktı:
"""
> python string-metotlari.py
    ['BTK akademi', ' python kursu ders notları']
"""

# ------------------------ #

outcome_index = message.index("akademi")
# Çıktı:
"""
> python string-metotlari.py
    4
"""

# ------------------------ #

outcome_startswith = message.startswith("B")
# Çıktı:
"""
> python string-metotlari.py
    True
"""

outcome_start_s_with = message.startswith("b")
# Çıktı:
"""
> python string-metotlari.py
    False
"""

# ------------------------ #

outcome_endswith = message.endswith("ı")
# Çıktı:
"""
> python string-metotlari.py
    True
"""

# outcome_end_s_with = message.endswith("s")
# Çıktı:
"""
> python string-metotlari.py
    False
"""

# ------------------------ #

outcome_replace = message.replace("python", "Python")
# Çıktı:
"""
> python string-metotlari.py
    BTK akademi, Python kursu ders notları
"""

# ------------------------ #

outcome_find = message.find("python")
# Çıktı:
"""
> python string-metotlari.py
    13
"""

# ------------------------ #

outcome = message # print için düzeltme

print(outcome)
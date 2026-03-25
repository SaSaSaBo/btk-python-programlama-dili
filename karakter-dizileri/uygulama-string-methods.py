"""
1. ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.
2. course_name değişkenindeki tüm karakterleri küçük harfe çeviriniz.
3. website değişkeninde kaç tane '.' karakteri vardır?
4. website değişkeni 'https' ile mi başlıyor?
5. website 'tr' ile mi bitiyor?
6. course_name içerisindeki tüm karakterler harflerden mi oluşuyor?
7. course_name değişkenindeki tüm boşlukları '-' ile değiştiriniz.
8. course_name değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
9. website değişkeni 'www' içeriyor mu?
10. course_name değişkenini listeye çeviriniz.
"""

course_name = "Btk Akademi Python ile Programlama Dersleri"
course_name_alpha = "BtkAkademiPythonileProgramlamaDersleri"
website = "https://www.btkakademi.gov.tr/"

# 1. Soru:
original = " Btk Akademi "
strip = original.strip()
print("original: " + "'" + original + "'")
print("strip: " + "'" + strip + "'")
# Çıktı:
"""
> python uygulama-string-methods.py
    original: ' Btk Akademi '
    strip: 'Btk Akademi'
"""
print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
lower = course_name.lower()
print("lower: " + "'" + lower + "'")
# Çıktı:
"""
> python uygulama-string-methods.py
    lower: 'btk akademi python ile programlama dersleri'
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
count = website.count(".")
print("count: " + str(count))
# Çıktı:
"""
> python uygulama-string-methods.py
    count: 3
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
startswith = website.startswith("https")
print("startswith: " + str(startswith))
# Çıktı:
"""
> python uygulama-string-methods.py
    startswith: True
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
endswith = website.endswith("tr")
print("endswith: " + str(endswith))
# Çıktı:
"""
> python uygulama-string-methods.py
    endswith: False
"""

print("# ------------------------ #")
# ------------------------ #

# 6. Soru:
isalpha = course_name_alpha.isalpha() # boşluk olduğunda sonuç False döner
print("isalpha: " + str(isalpha))
# Çıktı:
"""
> python uygulama-string-methods.py
    isalpha: True
"""

print("# ------------------------ #")
# ------------------------ #

# 7. Soru:
replace = course_name.replace(" ", "-")
print("replace: " + "'" + replace + "'")
# Çıktı:
"""
> python uygulama-string-methods.py
    replace: 'Btk-Akademi-Python-ile-Programlama-Dersleri'
"""

print("# ------------------------ #")
# ------------------------ #

# 8. Soru:
replace_word = course_name.replace("Python", "ReactJs")
print("replace_word: " + "'" + replace_word + "'")
# Çıktı:
"""
> python uygulama-string-methods.py
    replace_word: 'Btk Akademi ReactJs ile Programlama Dersleri'
"""

print("# ------------------------ #")
# ------------------------ #

# 9. Soru:
find = website.find("www")
index = website.index("tr")
print("find: " + str(find)) # eğer sonuç bulamazsa "-1" değerini geri gönderir
print("index: " + str(index)) # eğer sonuç bulamazsa geriye bir hata objesi gönderir
# Çıktı:
"""
> python uygulama-string-methods.py
    find: 8
    index: 27
"""

print("# ------------------------ #")
# ------------------------ #

# 10. Soru:
split = course_name.split()
print("split: " + "'" + str(split) + "'")
# Çıktı:
"""
> python uygulama-string-methods.py
    split: '['Btk', 'Akademi', 'Python', 'ile', 'Programlama', 'Dersleri']'
"""
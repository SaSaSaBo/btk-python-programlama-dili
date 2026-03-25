"""
1. Girilen 2 sayıdan hangisi büyüktür?
2. Girilen bir sayının tek çift kontrolünü yapınız.
3. Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.
"""

# 1. Soru:
number_1 = int(input("Sayı 1: "))
number_2 = int(input("Sayı 2: "))
outcome_is_greater = number_1 > number_2

print(f"{number_1}, {number_2}'den büyüktür: {outcome_is_greater}")
# Çıktı:
"""
> python uygulama-karsilastirma-operatorleri.py
    Sayı 1: 5
    Sayı 2: 3
    5, 3'den büyüktür: True
"""

print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
number_first = int(input("Sayı: "))

outcome_is_even = number_first % 2 == 0

print(f"{number_first} çifttir: {outcome_is_even}")
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    Sayı: 10
    10 çifttir: True
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
grade_1 = int(input("Grade 1: "))
grade_2 = int(input("Grade 2: "))
grade_3 = int(input("Grade 3: "))
outcome_average = (grade_1 + grade_2 + grade_3) / 3
outcome_is_greater_than_average = outcome_average > 50
# outcome_is_greater_than_average = outcome_average >= 50

print(f"Öğrencinin ortalaması: {outcome_average} öğrencinin başarısı belirtilen ortalama 50'den büyüktür: {outcome_is_greater_than_average}")
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    Grade 1: 75
    Grade 2: 40
    Grade 3: 60
    Öğrencinin ortalaması: 58.333333333333336 öğrencinin başarısı belirtilen ortalama 50'den büyüktür: True
    # ------------------------ #
    Grade 1: 50
    Grade 2: 30
    Grade 3: 40
    Öğrencinin ortalaması: 40.0 öğrencinin başarısı belirtilen ortalama 50'den büyüktür: False
"""
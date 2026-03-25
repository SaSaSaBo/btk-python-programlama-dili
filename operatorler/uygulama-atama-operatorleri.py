"""
1. Kullanıcıdan aldığınız 2 sayının çarpımı ile a, b, c toplamının farkı nedir?
2. c'nin b'ye kalansız bölümüni hesaplayınız.
3. (a, b, c) toplamının mod 7'si nedir?
4. b'nin a. kuvvetini hesaplayınız.
5. d, *e, f = (2, 4, 6, 8, 13) işlemine göre f'nin küpü nedir?
6. g, h, *i = (2, 4, 6, 8, 13) işlemine göre i'nin değerleri toplamı nedir?
"""

a, b, c = 4, 8, (12, 2)

# 1. Soru:
number_1 = int(input("Sayı 1: "))
number_2 = int(input("Sayı 2: "))
multiplication = number_1 * number_2
total_sum = a + b + (c[0] + c[1])
outcome = multiplication - total_sum

print("Kullanıcıdan alınan 2 sayının çarpımı: " + str(multiplication))
print("a, b, c toplamları: " + str(total_sum))
print("Kullanıcıdan alınan 2 sayının çarpımı ve a, b, c toplamının farkı: " + str(outcome))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    Sayı 1: 3
    Sayı 2: 25
    Kullanıcıdan alınan 2 sayının çarpımı: 75
    a, b, c toplamları: 26
    Kullanıcıdan alınan 2 sayının çarpımı ve a, b, c toplamının farkı: 49
"""

print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
outcome_full_divine = (c[0] + c[1]) // b
outcome_full_divine_1 = c[0] // b
outcome_full_divine_2 = c[1] // b

print("outcome_full_divine: " + str(outcome_full_divine))
print("outcome_full_divine_1: " + str(outcome_full_divine_1))
print("outcome_full_divine_2: " + str(outcome_full_divine_2))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    outcome_full_divine: 1
    outcome_full_divine_1: 1
    outcome_full_divine_2: 0
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
outcome_remainder = total_sum % 7

print("outcome_remainder: " + str(outcome_remainder))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    outcome_remainder: 5
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
outcome_power = b ** a

print("outcome_power: " + str(outcome_power))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    outcome_power: 4096
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
d, *e, f = (2, 4, 6, 8, 13) # a = 2, f = 13, e = (4, 6, 8)
outcome_power_for_f = f ** 3

print("outcome_power_for_f: " + str(outcome_power_for_f))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    outcome_power_for_f: 2197
"""

print("# ------------------------ #")
# ------------------------ #

# 6. Soru:
g, h, *i = (2, 4, 6, 8, 13) # g = 2, h = 4, i = (6, 8, 13)
total_sum_for_i = (i[0] + i[1] + i[2])

print("total_sum_for_i: " + str(total_sum_for_i))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    total_sum_for_i: 27
"""
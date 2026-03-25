"""
Birden fazla karşılaştırmayı birleştirmek için kullanılır.
1. and (VE): Her iki şart da Doğru olmalıdır.

Senaryo: Sisteme girmek için Kullanıcı Adı VE Şifre doğru olmalı.
"""
# (5 > 3) and (10 > 2)  # True ve True -> Sonuç: True
# (5 > 3) and (2 > 10)  # True ve False -> Sonuç: False
"""
2. or (VEYA): Şartlardan en az biri Doğru olsa yeterlidir.

Senaryo: Ödeme yapmak için Nakit VEYA Kartın olması yeterli.
"""
# (5 > 3) or (2 > 10)   # True veya False -> Sonuç: True
"""
3. not (DEĞİL): Sonucu tersine çevirir. True ise False, False ise True yapar. python not (5 > 3) # Normalde True ama 'not' olduğu için -> False
"""


# ------------------------ #

# (age >= 18) => true, false
# (mezuniyet == "lise") ya da (mezuniyet == "üniversite") => true, false
# outcome = (age >= 18) ve (mezuniyet == "lise" ve ya mezuniyet == "üniversite")

x = 11
outcome_and = (x > 5) and (x < 10)

print("outcome_and: " + str(outcome_and))
# Çıktı:
"""
> python mantiksal-operatorleri.py.py
    outcome_and: False
# ------------------------ #
True, True -> True
True, False -> False
False, False -> False
"""

# ------------------------ #

outcome_or = (x > 0) or (x % 2 == 0)

print("outcome_or: " + str(outcome_or))
# Çıktı:
"""
> python mantiksal-operatorleri.py.py
    outcome_or: True
# ------------------------ #
True, True -> True
True, False -> True # birden fazla False olsa dahi 1 adet True varsa sonuç True'dur.
False, False -> False
"""

# ------------------------ #

outcome_not = not(x > 0)

print("outcome_not: " + str(outcome_not))
# Çıktı:
"""
> python mantiksal-operatorleri.py.py
    outcome_not: False
# ------------------------ #
True -> False
False -> True
"""
"""
Hayatta her zaman sadece iki seçenek yoktur. Bazen 3, 4 veya daha fazla ihtimali kontrol etmemiz gerekir. Burada elif (else if kısaltması) devreye girer.
Mantık sırayla işler:
1. if'e bakar. Doğruysa yapar ve çıkar.
2. Yanlışsa elif'e bakar. Doğruysa yapar ve çıkar.
3. Hiçbiri tutmazsa en son else çalışır.
"""
# notu = 65
#
# if notu >= 85:
#     print("Pek iyi")
# elif notu >= 70:
#     print("İyi")
# elif notu >= 50:
#     print("Geçti")
# else:
#     print("Kaldı") # Yukarıdakilerin hiçbiri tutmadıysa burası çalışır.


# ------------------------ #

email = "sasa@gmail.com"
password = "148200"
if email == "sasa@gmail.com" :
    print("Email yanlış.")
elif password != "148200" :
    print("Şifre yanlış.")
else :
    print("Giriş yapıldı.")
# Çıktı:
"""
> python if-elseif.py
    Email yanlış.
"""

# ------------------------ #

x = 10
y = 20
# x = 30
# y = 20
# x = 30
# y = 30
if x < y :
    print("x, y'den küçüktür.")
elif y < x :
    print("y, x'den küçüktür.")
else :
    print("x ve y eşittir")
# Çıktı:
"""
> python if-elseif.py
    x, y'den küçüktür.
    # y, x'den küçüktür.
    # x ve y eşittir
"""
"""
İki değeri kıyaslar ve sonuç olarak sadece True (Doğru) veya False (Yanlış) üretir. Bu konu if-else bloklarının temelidir.

Operatör          |          Anlamı          |         Örnek (a=10, b=5)        |            Sonuç
==                |          Eşit mi?        |             a == b               |            False
!=                |        Eşit Değil mi?    |             a != b               |            True
>                 |          Büyük mü?       |             a > b                |            True
<                 |          Küçük mü?       |             a < b                |            False
>=                |    Büyük veya Eşit mi?   |             a >= 10              |            True
<=                |    Küçük veya Eşit mi?   |             b <= 5               |            True

Dikkat: a = 5 (Atama) ile a == 5 (Sorgulama) tamamen farklıdır. Karıştırmamaya dikkat et.
"""


# ------------------------ #

a, b, c, d = 3, 3, 25, 18
outcome_is_equal = a == b
outcome_is_not_equal = a != c
outcome_is_greater_than_b = c > b
outcome_is_lower_than_c = c < a
outcome_is_equal_or_greater_than_b = c >= b
outcome_is_not_equal_or_lower_than_c = c <= b

print("a, b değerine eşit mi: " + str(outcome_is_equal))
print("a, c değerine eşit değil mi: " + str(outcome_is_not_equal))
print("c, b değerinden büyük mü: " + str(outcome_is_greater_than_b))
print("a, c değerinden küçük mü: " + str(outcome_is_lower_than_c))
print("c, b değerinden büyük veya eşit mi: " + str(outcome_is_equal_or_greater_than_b))
print("b, c değerinden küçük veya eşit mi: " + str(outcome_is_not_equal_or_lower_than_c))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    a, b değerine eşit mi: True
    a, c değerine eşit değil mi: True
    c, b değerinden büyük mü: True
    a, c değerinden küçük mü: False
    c, b değerinden büyük veya eşit mi: True
    b, c değerinden küçük veya eşit mi: False
"""

# ------------------------ #

email = "sasasabo@gmail.com"
password = "148200"
get_email = input("email: ")
get_password = input("password: ")
outcome_email = (email == get_email)
outcome_password = (password == get_password)

print("Veri tabanında kayıtlı olan email: " + str(email) + " - " + "Girilen email adresi ile karşılaştırma sonucu: " + str(outcome_email))
print("Veri tabanında kayıtlı olan password: " + str(password) + " - " + "Girilen password ile karşılaştırma sonucu: " + str(outcome_password))
# Çıktı:
"""
> python uygulama-atama-operatorleri.py
    email: sasasabo@gmail.com
    password: 148200
    Veri tabanında kayıtlı olan email: sasasabo@gmail.com - Girilen email adresi ile karşılaştırma sonucu: True
    Veri tabanında kayıtlı olan password: 148200 - Girilen password ile karşılaştırma sonucu: True
"""
"""
Matematik dersinden bildiğimiz dört işlem ve Python'a özel birkaç ekstra işlemcidir.

Operatör          |           Anlamı             |          Örnek           |           Sonuç
+                 |          Toplama             |          3 + 2           |             5
-                 |          Çıkarma             |          3 - 2           |             1
*                 |           Çarpma             |          3 * 2           |             6
/                 |            Bölme             |          10 / 2          |       5.0 (Her zaman float döner)
%                 |          Mod (Kalan)         |          10 % 3          |      1 (10'un 3'e bölümünden kalan)
**                |            Üs Alma           |          2 ** 3          |             8
//                |           Tam Bölme          |          10 // 3         |       3 (Virgülden sonrasını atar)

İpucu: Mod operatörü (%), bir sayının tek mi çift mi olduğunu bulmak için çok kullanılır (sayi % 2 == 0 ise çifttir).
"""


# ------------------------ #

a = 5
b = 3

outcome_sum = a + b
outcome_minus = a - b
outcome_multiplication = a * b
outcome_divine = a / b
outcome_remainder = a % b
outcome_power = a ** b
outcome_full_divine = a // b

print("Toplama: ", outcome_sum)
print("Çıkarma: ", outcome_minus)
print("Çarpma: ", outcome_multiplication)
print("Kalanlı Bölme: ", outcome_divine)
print("Bölmeden Kalan: ", outcome_remainder)
print("Üs Alma: ", outcome_power)
print("Tam Bölme: ", outcome_full_divine)
# Çıktı:
"""
> python aritmatik-operatorler.py
    Toplama:  8
    Çıkarma:  2
    Çarpma:  15
    Kalanlı Bölme:  1.6666666666666667
    Bölmeden Kalan:  2
    Üs Alma:  125
    Tam Bölme:  1
"""
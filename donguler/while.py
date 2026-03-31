"""
For döngüsü bir liste bitince durur. While döngüsü ise verilen koşul doğru olduğu sürece dönmeye devam eder. Listeye bağlı değildir, şarta bağlıdır.
Tehlike: Eğer koşul hiç False olmazsa, program sonsuza kadar çalışır (Sonsuz Döngü - Infinite Loop).
"""
# x = 0
#
# while x < 3:
#     print(x)
#     x += 1  # Bunu yazmazsak x hep 0 kalır ve döngü asla bitmez!


# ------------------------ #
i = 0

while i < 10 :
    print(i)
    i += 1
# Çıktı:
"""
> python while.py
    0
    1
    2
    3
    4
    5
    6
    7
    8
"""

# ------------------------ #

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0

while x < len(numbers) :
    print(numbers[x])
    x += 1
# Çıktı:
"""
> python while.py
    1
    2
    3
    4
    5
    6
    7
    8
"""
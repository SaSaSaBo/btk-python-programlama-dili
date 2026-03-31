"""
1. Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
2. (1-100) aeasındaki sayıları azalan şekilde yazdırınız.
3. Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
4. Klavyeden girişi istenen username bilgisi için boşluk girildipği sürece tekrar username girişi isteyiniz.
5. Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
    dictionary listesi yapısı (student_no, student_name, student_surname) şeklinde olsun.
    Öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.
"""

# 1. Soru:
# beginning = int(input("Başlangıç: "))
# ending = int(input("Bitiş: "))
# i = beginning
#
# while i < ending :
#     if i % 2 == 0 :
#         print(i)
#     i += 1
# Çıktı:
"""
> python uygulama-while.py
    Başlangıç: 8
    Bitiş: 18
    8
    10
    12
    14
    16
"""

print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
# x = 100
#
# while x > 0 :
#     print(x)
#     x -= 1
# Çıktı:
"""
> python uygulama-while.py
    100
    99
    98
    97
    96
    95
    94
    93
    92
    ...
    17
    16
    15
    14
    13
    12
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
# s = 0
# numbers = []
#
# while s < 5 :
#     number = int(input("Sayı: "))
#     numbers.append(number)
#     s += 1
# numbers.sort()
#
# print(numbers)
# Çıktı:
"""
> python uygulama-while.py
    Sayı: 8
    Sayı: 5
    Sayı: 2
    Sayı: 3
    Sayı: 4
    [2, 3, 4, 5, 8]
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
# username = ""
#
# while not username :
#     username = input("Kullanıcı adı: ")
#
# print("Girilen kullanıcı adı: " + username)
# Çıktı:
"""
> python uygulama-while.py
    Kullanıcı adı: 
    Kullanıcı adı: sasa
    Girilen kullanıcı adı: sasa
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
is_continuous = "e"
students = []

while is_continuous != "h" :
    student_no = input("Öğrenci no: ")
    student_name = input("Öğrenci Adı: ")
    student_surname = input("Öğrenci Soyadı: ")

    students.append({"student_no": student_no,"student_name": student_name,"student_surname": student_surname})

    is_continuous = input("Devam mı? (e/h)")

for student in students :
    print(f"{student['student_no']} numaralı öğrencinin adı: {student['student_name']} {student['student_surname']}")
# Çıktı:
"""
> python uygulama-while.py
    Öğrenci no: 31097
    Öğrenci Adı: Christopher Chan
    Öğrenci Soyadı: Bang    "
    Devam mı? (e/h)e
    Öğrenci no: 251098
    Öğrenci Adı: Minho
    Öğrenci Soyadı: Lee
    Devam mı? (e/h)e
    Öğrenci no: 11899
    Öğrenci Adı: Changbin
    Öğrenci Soyadı: Seo
    Devam mı? (e/h)h
    31097 numaralı öğrencinin adı: Christopher Chan Bang
    251098 numaralı öğrencinin adı: Minho Lee
    11899 numaralı öğrencinin adı: Changbin Seo
"""
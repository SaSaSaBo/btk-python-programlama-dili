"""
1. Yaşı 18'den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.
2. Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
3. Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
4. İşe girmek için en az önlisans ya da lisansmezunu olma durumunu kontrol ediniz. Sigara kkullanmama koşulu.
5. Uygulamaya giriş kontrolünü "username ya da email" ve "parola" için yapalım.
"""

# 1. Soru:
parent_permission = True
age = 17
outcome_check = parent_permission or (age >=  18)

print("outcome_check: " + str(outcome_check))
# Çıktı:
"""
> python uygulama-mantiksal-operatorler.py
    outcome_check: True
"""

print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
grade_1, grade_2, grade_3 = (50, 40, 80)
outcome_is_middle = (grade_1 >= 50) and (grade_1 <= 100)

print("Ders geçme durumu: " + str(outcome_is_middle))
# Çıktı:
"""
> python uygulama-mantiksal-operatorler.py
    Ders geçme durumu: True
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
average = 70
failed_lessons = 0
outcome_pass = (average > ((grade_1 + grade_2 + grade_3) / 3)) and (failed_lessons == 0)

print("Öğrencinin geçme durumu: " + str(outcome_pass))
# Çıktı:
"""
> python uygulama-mantiksal-operatorler.py
    Öğrencinin geçme durumu: True
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
education = "lise"
smoke = False
outcome_info = ((education == "önlisans") or (education == "lisans")) and not smoke

print("İşe girme durumu: " + str(outcome_info))
# Çıktı:
"""
> python uygulama-mantiksal-operatorler.py
    İşe girme durumu: False
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
email = "sasa@gmail.com"
username = "sasa"
password = "148200"
get_email_username = input("Kullanıcı adı ya da email: ")
get_password = input("Şifre: ")
outcome_login = ((email == get_email_username) or (username == "sasa")) and (password == get_password)

print("Kullanıcı giriş yapabildi: " + str(outcome_login))
# Çıktı:
"""
> python uygulama-mantiksal-operatorler.py
    Kullanıcı adı ya da email: sasa
    Şifre: 148200
    Kullanıcı giriş yapabildi: True
# ------------------------ #
    Kullanıcı adı ya da email: sasa
    Şifre: 1482
    Kullanıcı giriş yapabildi: False
"""
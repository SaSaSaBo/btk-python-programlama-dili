"""
Programlamada "Eğer şu olursa bunu yap, olmazsa şunu yap" mantığıdır. Günlük hayattan örnek:
Hava yağmurlu mu?
Evet: Şemsiyeni al.
Hayır: Güneş gözlüğünü al.

Bilgisayar sadece True (Doğru) veya False (Yanlış) cevabına göre hareket eder. (Burada 7. Bölümde öğrendiğin Karşılaştırma Operatörleri devreye girer).
if / else Blokları
İki ihtimalli durumlar için kullanılır.
if (Eğer): Yanındaki koşul True ise çalışır.
else (Değilse): if koşulu False ise (yani sağlanmadıysa) devreye girer.
⚠️ Çok Önemli Kural: Girinti (Indentation) Python'da süslü parantez {} yoktur. Bir kodun if bloğuna ait olduğunu belirtmek için bir "Tab" tuşu kadar içeriden yazmalısın.
"""
# yas = 17
#
# if yas >= 18:
#     print("Ehliyet alabilirsin.") # Girinti var, if'e ait.
# else:
#     print("Ehliyet alamazsın.")   # Girinti var, else'e ait.


# ------------------------ #

if True :
    print("True")
# Çıktı:
"""
> python if-else.py                            
    True
"""

# ------------------------ #

if 3 > 2 :
    print("3, 2'den büyük")
# Çıktı:
"""
> python if-else.py                            
    3, 2'den büyük
"""

# ------------------------ #

if 3 > 5 :
    print("3, 2'den büyük")
# Çıktı:
"""
> python if-else.py                            
    
"""

# ------------------------ #

outcome = 3 > 5
if outcome :
    print("3, 2'den büyük")
# Çıktı:
"""
> python if-else.py                            
    
"""

# ------------------------ #

login = True
if login :
    print("Giriş yapıldı.")
# Çıktı:
"""
> python if-else.py                            
    Giriş yapıldı.
"""

# ------------------------ #

email = "sasa@gmail.com"
password = "148200"
login = (email == "sasa@gmail.com") and (password == "148200")
if login :
    print("email ve şifre ile giriş yapıldı.")
# Çıktı:
"""
> python if-else.py                            
    email ve şifre ile giriş yapıldı.
"""

# ------------------------ #

login = (email == "sasa@gmail.com") and (password == "148201")
if login :
    print("email ve şifre ile giriş yapıldı.")
else :
    print("email ya da parola yanlış")
# Çıktı:
"""
> python if-else.py                            
    email ya da parola yanlış
"""

# ------------------------ #

login = (email == "sasa@gmail.com") and (password == "148200")
if not login :
    print("email ya da parola yanlış")
else :
    print("email ve şifre ile giriş yapıldı.")
# Çıktı:
"""
> python if-else.py                            
    email ve şifre ile giriş yapıldı.
"""

# ------------------------ #

if email == "sasa@gmail.com" :
    if password == "148201" :
        print("Giriş yapıldı.")
    else :
        print("Şifre yanlış.")
else :
    print("Email yanlış.")
# Çıktı:
"""
> python if-else.py                            
    Şifre yanlış.
"""
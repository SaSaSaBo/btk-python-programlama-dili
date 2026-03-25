"""
1. Değişken Nedir?
En basit tabiriyle değişken, verileri (data) bellekte tutmak için oluşturduğumuz isimlendirilmiş kutulardır.
Bir veriyi (sayı, metin, liste vb.) daha sonra kullanmak üzere bilgisayarın hafızasında (RAM) saklamamızı sağlar. Biz o veriye ulaşmak istediğimizde, değişkene verdiğimiz ismi çağırırız.

2. Değişken Nasıl Oluşturulur?
Python'da değişken oluşturmak için bir "tür" belirtmenize (C# veya Java'daki gibi int, string yazmanıza) gerek yoktur. Sadece bir isim verirsiniz ve değeri atarsınız.
Buna Dynamic Typing (Dinamik Tür Belirleme) denir. Python, verinin türünü otomatik olarak anlar.
Örnekler
maas = 5000              # Tam sayı (Integer)
vergi_orani = 0.18       # Ondalıklı sayı (Float)
isim = "Sabiha"           # Metin (String)
ogrenci_mi = False        # Mantıksal (Boolean)

3. Atama Operatörü (=)
Matematikteki "eşittir" ile programlamadaki = işareti aynı değildir.
Programlamada = işareti "sağdaki değeri al, soldaki ismin içine koy" demektir.
sayi = 10  # 10 değerini 'sayi' değişkenine ata.
sayi = 20  # 'sayi' değişkeninin değeri artık 20 oldu (Eski değer silindi).
"""


# ------------------------ #
print("Girilecek input: ")
message = input()
print("Çıktı: ")
print("Hello " + message)

# Çıktı:
"""
> python degisken-nedir.py
    Girilecek input: 
    We are Stray Kids!!
    Çıktı: 
    Hello We are Stray Kids!!
"""
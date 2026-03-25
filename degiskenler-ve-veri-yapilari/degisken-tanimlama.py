"""
4. Değişken Tanımlama Kuralları (Çok Önemli)
Derste üzerinde en çok durulan kısım genellikle isimlendirme kurallarıdır. Hata almamak için şunlara dikkat etmelisin:
Rakamla Başlayamaz: 1sayi = 10 (Hatalı) -> sayi1 = 10 (Doğru).
Boşluk İçeremez: ad soyad = "Ali" (Hatalı) -> ad_soyad veya adSoyad kullanılmalı.
Türkçe Karakter Kullanmamaya Çalışın: Python 3 desteklese de, standart olarak ığüşöç gibi harfler yerine igusoc kullanmak profesyonel bir alışkanlıktır (yas yerine age veya yas gibi).
Özel Kelimeler Kullanılamaz: Python'un kendi komutları değişken ismi olamaz (örn: if, for, True, class).
Büyük/Küçük Harf Duyarlıdır (Case Sensitive):
age = 20
Age = 30
Bu ikisi Python için tamamen farklı iki değişkendir.

5. İsimlendirme Standartları
Zorunlu olmasa da Python yazılımcıları arasında kabul görmüş bir standart vardır: Snake Case. Kelimeler tamamen küçük harfle yazılır ve aralarına alt çizgi (_) konur.
UrunFiyati (Yanlış değil ama Python tarzı değil)
urun_fiyati (Pythonic - Doğru kullanım)

6. Basit Birleştirme
Değişkenleri tanımladıktan sonra onları print fonksiyonu ile ekrana yazdırabilir veya işlem yapabilirsin.
ad = "Sabiha"
soyad = "Akgün"

İki string değişkeni toplamak onları yan yana getirir
print(ad + " " + soyad)
Çıktı: Ayşe Yılmaz

Özet Tablo
-----------------------------------------------------------------------
    Özellik      |            Açıklama
Tanımlama        |    degisken_adi = deger
Tür Belirleme    |    Otomatiktir (Yazmaya gerek yok).
Büyük/Küçük Harf |    Duyarlıdır (a ve A farklıdır).
Başlangıç        |    "Sayı ile başlayamaz, harf veya _ ile başlamalı."
"""


# ------------------------ #
# 2000 + 2000 * %18

urunAFiyat = 4000
urunBFiyat = 3000
kdvOrani = 0.20

print(urunAFiyat + (urunAFiyat * kdvOrani)) # ürün A
print(urunBFiyat + (urunBFiyat * kdvOrani)) # ürün B

urunToplami = urunAFiyat + urunBFiyat
print(urunToplami + (urunToplami * kdvOrani))

# Çıktı:
"""
> python degisken-tanimlama.py
    4800.0
    3600.0
    8400.0
"""
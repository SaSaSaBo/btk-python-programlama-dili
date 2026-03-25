"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın KDV oranı nedir? (%18)

Sabiha Ayşe Akgün
0505 123 45 82
sasastaaallain@gmail.com
Kocaeli

Satın alınan ürünler

Ürün adı: SKZ IT TAPE 'DO IT' ('IT VER.')
Fiyatı: 1.204 TL

Ürün adı: SKZ IT TAPE 'DO IT' ('DO VER.')
Fiyatı: 858 TL

Ürün adı: DO IT DIGITAL ALBUM
Fiyatı: 346 TL
"""

customer_name = "Sabiha Ayşe"
customer_surname = "Akgün"
customer_no = "05051234582"
customer_email = "sasastaaallain@gmail.com"
customer_address = "Kocaeli"

product_name1 = "SKZ IT TAPE 'DO IT' ('IT VER.')"
product_name2 = "SKZ IT TAPE 'DO IT' ('DO VER.')"
product_name3 = "DO IT DIGITAL ALBUM"

product_cost1 = 1204
product_cost2 = 858
product_cost3 = 346

total_paying_cost = product_cost1 + product_cost2 + product_cost3
# ("Toplam Ödenen Fiyat: " + total_paying_cost) -> total_paying_cost değeri aslen number olduğu için string ifadenin sonuna + operotörü aracığıyla yanlızca string ifade koyulabilir
# 1. Yöntem:
print("Toplam Ödenen Fiyat: " + str(total_paying_cost))
# 2. Yöntem:
# print(f"Toplam Ödenen Fiyat: {total_paying_cost}")
# 3. Yöntem:
# print("Toplam Ödenen Fiyat:", total_paying_cost)

print("Toplam KDV Oranı: " + str(total_paying_cost * 0.18))

# Çıktı:
"""
> python uygulama-degiskenler.py
    Toplam Ödenen Fiyat: 2408
    Toplam KDV Oranı: 433.44
"""
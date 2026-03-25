"""
1. 'bangchan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
2. Son eklenen siparişi siliniz.
3. Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
    '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır
4. Müşterileri alfabedik olarak sıralayınız.
5. Sipraiş toplamlarını azalan şekilde sıralayınız.
6. En düşük sipariş hangisidir?
7. 'bangchan' isimli kullanıcının kaç tane siparişi vardır?
8. Customers listesinden 'leeknow' isimli kullanıcıyı siliniz.
9. Listelerdeki tüm içerikleri siliniz.
10. Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.
"""

customers = ["cb97", "leeknow", "spearB", "jOne", "I.N"]
order_totals = [1000000, 120000, 180000, 170000, 100000]

# 1. Soru:
customers.append("cb97")
order_totals.append(500000)

print("Yeni Müşteri listesi: " + str(customers))
print("Güncelleşmiş sipariş sonucu: " + str(order_totals))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Yeni Müşteri listesi: ['cb97', 'leeknow', 'spearB', 'jOne', 'I.N', 'cb97']
    Güncelleşmiş sipariş sonucu: [1000000, 120000, 180000, 170000, 100000, 500000]
"""
print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
customers.pop()
order_totals.pop()

print("Müşteri listesinden son eleman silindi: " + str(customers))
print("Güncellenen sipariş sonucu: " + str(order_totals))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Müşteri listesinden son eleman silindi: ['cb97', 'leeknow', 'spearB', 'jOne', 'I.N']
    Güncellenen sipariş sonucu: [1000000, 120000, 180000, 170000, 100000]
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
outcome = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0]} liradır."

print("outcome: " + outcome)
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    outcome: cb97 isimli müşterinin sipariş toplamı 1000000 liradır.
    # outcome: cb97 isimli müşterinin sipariş toplamı 1500000 liradır.
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
customers.sort()
print("Alfabetik müşteri listesi: " + str(customers))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Alfabetik müşteri listesi: ['I.N', 'cb97', 'jOne', 'leeknow', 'spearB']
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
order_totals.sort()
order_totals.reverse()

print("Sıralı sipariş listesi: " + str(order_totals))
print("Tersten sipariş listesi: " + str(order_totals))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Sıralı sipariş listesi: [1000000, 180000, 170000, 120000, 100000]
    Tersten sipariş listesi: [1000000, 180000, 170000, 120000, 100000]
"""

print("# ------------------------ #")
# ------------------------ #

# 6. Soru:
outcome = min(order_totals)

print("En düşük sipariş totali: " + str(outcome))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    En düşük sipariş totali: 100000
"""

print("# ------------------------ #")
# ------------------------ #

# 7. Soru:
outcome = customers.count("cb97")

print("cb97 müşterisinin sipariş sayısı: " + str(outcome))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    cb97 müşterisinin sipariş sayısı: 2
"""

print("# ------------------------ #")
# ------------------------ #

# 8. Soru:
customers.remove("leeknow")
order_totals.remove(120000)

print("Yeni müşteri listesi: " + str(customers))
print("Yeni sipariş tutarı listesi: " + str(order_totals))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Yeni müşteri listesi: ['I.N', 'cb97', 'jOne', 'spearB']
    Yeni sipariş tutarı listesi: [1000000, 180000, 170000, 100000]
"""

print("# ------------------------ #")
# ------------------------ #

# 9. Soru:
customers.clear()
order_totals.clear()

print("Silinen müşteri listesi: " + str(customers))
print("Silinen sipariş listesi: " + str(order_totals))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Silinen müşteri listesi: []
    Silinen sipariş listesi: []
"""

print("# ------------------------ #")
# ------------------------ #

# 10. Soru:
username = input("Müşteri adı: ")
order_total = int(input("Sipariş tutarı: "))
customers.append(username)
order_totals.append(order_total)

print("Yeni Müşteri listesi: " + str(customers))
print("Yeni sipariş tutarı listesi: " + str(order_totals))
# Çıktı:
"""
> python uygulama-liste-metotlari.py
    Yeni Müşteri listesi: ['I.N', 'cb97', 'jOne', 'spearB', 'hyunjin']
    Yeni sipariş tutarı listesi: [1000000, 180000, 170000, 100000, 1300000]
"""
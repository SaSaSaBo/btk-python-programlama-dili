"""
enumerate() Metodu
📌 Tanım: enumerate(), iterable (liste, tuple vb.) içindeki her elemana otomatik olarak bir index (sıra numarası) ekler.

🧠 Mantık: Eleman ve index birlikte elde edilir.

📌 Açıklama
Döngü sırasında hem elemanın kendisine hem de kaçıncı sırada olduğuna aynı anda erişmeyi sağlar.
Varsayılan olarak index 0’dan başlar.
İstenirse başlangıç değeri değiştirilebilir.
range(len()) kullanımına alternatif olarak daha temiz ve okunabilir bir yöntem sunar.
⚠️ Not
Çıktı yapısı (index, değer) şeklindedir
Kod okunabilirliğini artırır

🔹 zip() Metodu
📌 Tanım: zip(), birden fazla iterable’ı aynı anda birleştirerek, elemanlarını aynı indexlerine göre eşleştirir.

🧠 Mantık: Aynı sıradaki elemanlar birlikte işlenir.

📌 Açıklama
Birden fazla listeyi paralel şekilde dolaşmayı sağlar.
Her iterasyonda, verilen iterable’lardaki aynı indexte bulunan elemanları birlikte döndürür.
İki veya daha fazla iterable ile kullanılabilir.
⚠️ Not
İşlem, verilen iterable’lar arasındaki en kısa olanın uzunluğuna göre yapılır
Sonuç, eşleşmiş veri grupları şeklindedir

🔑 Kısa Özet
enumerate() → elemanlara index ekler
zip() → birden fazla iterable’ı eşleştirir
"""

# ------------------------ #


# index = 1
# brands = ["opel", "bmw", "togg"]

# for brand in brands :
#     print(f"{index} - {brand}")
#     index += 1
"""
    > python enumerate-zip.py
        1 - opel
        2 - bmw
        3 - togg
"""

# ------------------------ #

# obj1 = enumerate(brands)
#
# print(type(obj1))
# print(list(obj1))

"""
    > python enumerate-zip.py
        <class 'enumerate'>
        [(0, 'opel'), (1, 'bmw'), (2, 'togg')]
"""

# ------------------------ #

# obj1 = enumerate(brands, 1)
#
# print(type(obj1))
# print(list(obj1))

"""
    > python enumerate-zip.py
        <class 'enumerate'>
        [(1, 'opel'), (2, 'bmw'), (3, 'togg')]
"""

# ------------------------ #

# for index, brand in enumerate(brands, 1) :
#     print(f"{index} - {brand}")
"""
    > python enumerate-zip.py
        1 - opel
        2 - bmw
        3 - togg
"""

# ------------------------ #

# zip

number = [25, 3, 18]
student = ["BangChan", "LeeKnow", "Changbin"] # , "Hyunjin"]

print(list(zip(number, student)))
"""
    > python enumerate-zip.py
        [(25, 'BangChan'), (3, 'LeeKnow'), (18, 'Changbin')]
"""

# ------------------------ #

for stnd in zip(number, student) :
    print(stnd)
"""
    > python enumerate-zip.py
        (25, 'BangChan')
        (3, 'LeeKnow')
        (18, 'Changbin')
"""
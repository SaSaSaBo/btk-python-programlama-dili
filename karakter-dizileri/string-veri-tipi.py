"""
Stringler karakter dizileridir. Python'da tanımlamanın birkaç yolu vardır.

Tırnak İşaretleri: Tek tırnak (' ') veya çift tırnak (" ") kullanılabilir. İkisi de aynıdır, ancak metin içinde kesme işareti kullanacaksan çift tırnakla başlamak işi kolaylaştırır.
"""
# message = 'Merhaba'
# question = "Ali'nin evi nerede?"  # Çift tırnak dışarıda, tek tırnak içeride sorunsuz çalışır.
"""
Birleştirme (Concatenation): + operatörü metinleri yan yana yapıştırır.
Uzunluk: len() fonksiyonu boşluklar dahil karakter sayısını verir.
"""


# ------------------------ #

course_name = "Python ile Programlama"
course_description = "Python ile programlamaya başlangıç"
course_time = "12 saat 37 dakika"

message = "Kurs adı: " + course_name + ", " + "Kurs açıklaması: " + course_description + ", " + "Kurs Süresi: " + course_time

print(message)

# Çıktı:
"""
> python string-veri-tipi.py     
    Kurs adı: Python ile Programlama, Kurs açıklaması: Python ile programlamaya başlangıç, Kurs Süresi: 12 saat 37 dakika
"""

# ------------------------ #

print(message[-1])

# Çıktı:
"""
> python string-veri-tipi.py     
    a
"""

# ------------------------ #

print(message[0])

# Çıktı:
"""
> python string-veri-tipi.py     
    P
"""
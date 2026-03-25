"""
Listelere çok benzerler ama tek ve en önemli farkı: Tanımlandıktan sonra DEĞİŞTİRİLEMEZLER (Immutable).
Tanımlama: Normal parantez () kullanılır.
Kullanım Amacı: Veritabanı ayarları gibi programın çalışırken değişmesini istemediğimiz veriler için kullanılır.
"""
#liste = [1, 2]
# tup = (1, 2)
#
# liste[0] = 5  # ÇALIŞIR: Liste değişti.
# tup[0] = 5    # HATA! 'tuple' object does not support item assignment.

# ------------------------ #

my_list = [1, 8, 19, 25, 3, 18]
my_tuple = (1, 8, 19, 25, 3, 18) # değiştirilemez

print("my_list tipi: " + str(type(my_list)))
print("my_tuple tipi: " + str(type(my_tuple)))
# Çıktı:
"""
> python tuple-liste.py
    my_list tipi: <class 'list'>
    my_tuple tipi: <class 'tuple'>
"""

# ------------------------ #

my_list[0] = 1
outcome_list = my_list

print("my_list: " +  str(outcome_list))
# Çıktı:
"""
> python tuple-liste.py
    my_list: [3, 8, 19, 25, 3, 18]
"""

# my_tuple[0] = 3
outcome_tuple = my_tuple

print("my_tuple: " +  str(outcome_tuple))
# Çıktı:
"""
> python tuple-liste.py
    Traceback (most recent call last):
        File "/tuple-liste.py", line 38, in <module>
            my_tuple[0] = 3
            ~~~~~~~~^^^
    TypeError: 'tuple' object does not support item assignment
"""

# ------------------------ #

my_list.append(3)
my_list.append(10)
my_list.append(97)

print("Yeni my_list: " + str(my_list))
# Çıktı:
"""
> python tuple-liste.py
    Yeni my_list: [1, 8, 19, 25, 3, 18, 3, 10, 97]
"""

# my_tuple.append(97)

print("Yeni my_tuple: " + str(my_tuple))
# Çıktı:
"""
> python tuple-liste.py
    Traceback (most recent call last):
        File "/tuple-liste.py", line 65, in <module>                              
            my_tuple.append(97)
            ^^^^^^^^^^^^^^^
    AttributeError: 'tuple' object has no attribute 'append'
"""

# ------------------------ #

my_list_tuple = tuple([1, 8, 19, 25, 3, 18])

print("my_list_tuple tipi: " + str(type(my_list_tuple)))
# Çıktı:
"""
> python tuple-liste.py
    my_list_tuple tipi: <class 'tuple'>
"""

my_tuple_list = list((1, 8, 19, 25, 3, 18))

print("my_tuple_list tipi: " + str(type(my_tuple_list)))
# Çıktı:
"""
> python tuple-liste.py
    my_tuple_list tipi: <class 'list'>
"""
"""
Python'da her verinin bir "kimliği" vardır. Python, verinin ne olduğunu anlamak için bu kimliklere (türlere) bakar.
Temel Veri Tipleri:
int (Integer - Tam Sayı): Kesirli olmayan sayılardır.
Örnek: 5, -10, 0, 2023

float (Floating Point - Ondalıklı Sayı): Virgüllü (noktalı) sayılardır.
Örnek: 3.14, 0.001, -5.2, 10.0 (Sonunda .0 olsa bile float sayılır).

str (String - Metin): Tırnak işaretleri ("" veya '') içindeki her şeydir.
Örnek: "Ali", "123" (Tırnak içinde olduğu için matematiksel değeri yoktur, metindir).

bool (Boolean - Mantıksal): Sadece iki değer alır. Genellikle koşul durumlarında (If/Else) kullanılır.
Örnek: True (Doğru), False (Yanlış).

type() Fonksiyonu
Bir değişkenin hangi türde olduğunu merak ediyorsan type() komutunu kullanırsın
"""
# Örnek
# x = 10
# y = "10"
# z = 10.5
# print(type(x))  # Çıktı: <class 'int'>
# print(type(y))  # Çıktı: <class 'str'>
# print(type(z))  # Çıktı: <class 'float'>


# ------------------------ #
name = "Sabiha"
age = 23
weight = 60.5
isStudent = False

print(type(name)) # str
# |-> t = type(name)
# |-> print(t)
print(type(age)) # int
print(type(weight)) # float
print(type(isStudent)) # bool

print("ad: " + name + " age: " + str(age) + " weight: " + str(weight) + " isStudent: " + str(isStudent))

# Çıktı:
"""
> python veri-tipleri.py
    <class 'str'>
    <class 'int'>
    <class 'float'>
    <class 'bool'>
    ad: Sabiha age: 23 weight: 60.5 isStudent: False
"""
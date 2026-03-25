"""
Değişkenleri bir cümlenin içine dinamik olarak yerleştirme sanatıdır.
1. .format() Yöntemi (Eskimeye başladı ama bilmelisin): Süslü parantez {} yer tutucu olarak kullanılır.
"""
# ad = "Cafer"
# boy = 1.10
# print("Adım {} ve yaşım {}.".format(ad, yas))
"""
2. f-String (Modern ve Önerilen Yöntem): Javascript'teki "Template Literals" ( backtick ) mantığına çok benzer. Tırnağın başına f koyarsın ve değişkenleri direkt {} içine yazarsın
"""
# print(f"Adım {ad} ve yaşım {yas}.")


# ------------------------ #

# String Concat
name = "Christopher Chan"
surname = "Bhang"
age = 28
# message = "My name is " + name + " " + surname + "." + " And I'm " + str(age) + " years old" + "."
# Çıktı:
"""
> python string-formatlama.py
    My name is Christopher Chan Bhang.and I'm 28 years old.
"""

# String Format
# message = "My name is {} {}.and I'm {} years old.".format(name, surname, age)
# message = "My name is {0} {1}.and I'm {2} years old.".format(name, surname, age)
# message = "My name is {n} {s}.and I'm {a} years old.".format(n=name, s=surname, a=age)
# Çıktı:
"""
> python string-formatlama.py
    My name is Christopher Chan Bhang.and I'm 28 years old.
"""

# f-string
message = f"My name is {name} {surname}.and I'm {age} years old."
# Çıktı:
"""
> python string-formatlama.py
    My name is Christopher Chan Bhang.and I'm 28 years old.
"""

print(message)
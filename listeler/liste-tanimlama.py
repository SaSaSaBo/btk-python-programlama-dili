programming_languages = ["Python", "Java", "C++", "c#", "JavaScript"]

type = type(programming_languages)

print("type: " + str(type))
# Çıktı:
"""
> python liste-tanimlama.py
    type: <class 'list'>
"""

# ------------------------ #

slice = programming_languages[0:2]

print("slice: " + str(slice))
# Çıktı:
"""
> python liste-tanimlama.py
    slice: ['Python', 'Java']
"""

# ------------------------ #

# güncelleme yapmak için
programming_languages[-1] = "Php"
final = programming_languages
print("final: " + str(final))
# Çıktı:
"""
> python liste-tanimlama.py
    final: ['Python', 'Java', 'C++', 'c#', 'Php']
"""

# ------------------------ #

# ekleme yapmak için
add = programming_languages + ["Go", "Delphi"]

print("add: " + str(add))
# Çıktı:
"""
> python liste-tanimlama.py
    add: ['Python', 'Java', 'C++', 'c#', 'Php', 'Go', 'Delphi']
"""

# ------------------------ #

# koşul ifadeleri
question =  "Python" in programming_languages

print("question: " + str(question))
# Çıktı:
"""
> python liste-tanimlama.py
    question: True
"""

# ------------------------ #

# döngü
for l in programming_languages:
    print(l)
# Çıktı:
"""
> python liste-tanimlama.py
    Python
    Java
    C++
    c#
    Php
"""

# ------------------------ #

# silmek için
del programming_languages[2]

print("silinmiş hali: " + str(programming_languages))
# Çıktı:
"""
> python liste-tanimlama.py
    silinmiş hali: ['Python', 'Java', 'c#', 'Php']
"""
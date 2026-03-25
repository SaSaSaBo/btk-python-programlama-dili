"""
1. "Toyota, BMW, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
2. Liste kaç elemandır?
3. Listenin ilk ve son elemanı nedir?
4. "Renault" markasını "Togg" ile güncelleyiniz.
5. "Togg" listenin bir elemanı mıdır?
6. Listenin ilk 2 elemanını alınız.
7. Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
8. Listenin son elemanını siliniz.
9. Aşağıdaki verileri liste içerisinde saklayınız:
    student1: Bhang Chan 1997 [70, 80, 90]
    student2: Seo Changbin 1999 [70, 70, 90]
    student3: Lee Minho 1998 [80, 80, 90]
10. Öğrencilerin yaşlartını hesaplayınız.
11. Öğrencilerin not ortalamalarını hesaplayınız.
"""

# 1. Soru:
brand = ["Toyota", "BMW", "Renault", "Mercedes"]
print("markalar: " + str(brand))
# Çıktı:
"""
> python uygulama-listeler.py 
    markalar: ['Toyota', 'BMW', 'Renault', 'Mercedes']
"""
print("# ------------------------ #")
# ------------------------ #

# 2. Soru:
length = len(brand)
print("uzunluk: " + str(length))
# Çıktı:
"""
> python uygulama-listeler.py 
    uzunluk: 4
"""

print("# ------------------------ #")
# ------------------------ #

# 3. Soru:
first_element = brand[0]
last_element = brand[-1]
print("first element: " + str(first_element))
print("last element: " + str(last_element))
# Çıktı:
"""
> python uygulama-listeler.py 
    first element: Toyota
    last element: Mercedes
"""

print("# ------------------------ #")
# ------------------------ #

# 4. Soru:
brand[2] = "Togg"
update = brand
print("güncellenen: " + str(update))
# Çıktı:
"""
> python uygulama-listeler.py 
    güncellenen: ['Toyota', 'BMW', 'Togg', 'Mercedes']
"""

print("# ------------------------ #")
# ------------------------ #

# 5. Soru:
search = "Togg" in brand
# search = "Togg" not in brand
print("search: " + str(search))
# Çıktı:
"""
> python uygulama-listeler.py 
    search: True
    # search: False
"""

print("# ------------------------ #")
# ------------------------ #

# 6. Soru:
slice = brand[:2]
print("slice: " + str(slice))
# Çıktı:
"""
> python uygulama-listeler.py 
    slice: ['Toyota', 'BMW']
"""

print("# ------------------------ #")
# ------------------------ #

# 7. Soru:
add = brand +  ["Ford", "Citroen"]
print("add: " + str(add))
# Çıktı:
"""
> python uygulama-listeler.py 
    add: ['Toyota', 'BMW', 'Togg', 'Mercedes', 'Ford', 'Citroen']
"""

print("# ------------------------ #")
# ------------------------ #

# 8. Soru:
del brand[-1]
delete = brand
print("delete: " + str(delete))
# Çıktı:
"""
> python uygulama-listeler.py 
    delete: ['Toyota', 'BMW', 'Togg']
"""

print("# ------------------------ #")
# ------------------------ #

# 9. Soru:
student1 = ["Bhang", "Chan", 1997, [70, 80, 90]]
student2 = ["Seo", "Changbin", 1999, [70, 70, 90]]
student3 = ["Lee", "Minho", 1998, [80, 80, 90]]
# students = [student1, student2, student3]
# ya da
students = [["Bhang", "Chan", 1997, [70, 80, 90]], ["Seo", "Changbin", 1999, [70, 70, 90]], ["Lee", "Minho", 1998, [80, 80, 90]]]

print("öğrenci listesi: " + str(students))
# Çıktı:
"""
> python uygulama-listeler.py 
    öğrenci listesi: [['Bhang', 'Chan', 1997, [70, 80, 90]], ['Seo', 'Changbin', 1999, [70, 70, 90]], ['Lee', 'Minho', 1998, [80, 80, 90]]]
"""

print("# ------------------------ #")
# ------------------------ #

# 10. Soru:
today_date = 2026
students_age = [today_date - student[2] for student in students]

for i in range(len(students)):
    name = students[i][1]
    age = students_age[i]
    print(f"{name} {age} yaşında.")
# Çıktı:
"""
> python uygulama-listeler.py 
    Chan 29 yaşında.
    Changbin 27 yaşında.
    Minho 28 yaşında.
"""

print("# ------------------------ #")
# ------------------------ #

# 11. Soru:
students_average = [sum(student[3]) / len(student[3]) for student in students]
for student, age, ortalama in zip(students, students_age, students_average):
    student = student[1]
    # :.2f kodu, ortalamayı virgülden sonra 2 basamak göster demektir (Örn: 76.66)
    print(f"{student} - Not Ortalaması: {ortalama:.2f}")
# Çıktı:
"""
> python uygulama-listeler.py 
    Chan - Not Ortalaması: 80.00
    Changbin - Not Ortalaması: 76.67
    Minho - Not Ortalaması: 83.33
"""
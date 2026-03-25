"""
Aşağıdaki öğrencileri bilgilerini dictionary listesinde saklayınız.
    310 Christopher Bang Chan 1997 (75, 80, 75)
    251 Lee Minho 1998 (80, 80, 85)
    118 Seo Changbin 1999 (70, 75, 80)

Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.
    310 numaralı Christopher Bang Chan ismindeki öğrencinin yaşı 28 ve not ortalaması 77.
"""

students = {
    310: {
        "Name": "Christopher Chan",
        "Surname": "Bang",
        "Birth_date": 1997,
        "Grades": (75, 80, 75)
    },
    251: {
        "Name": "Minho",
        "Surname": "Lee",
        "Birth_date": 1998,
        "Grades": (80, 80, 85)
    },
    118: {
        "Name": "Changbin",
        "Surname": "Seo",
        "Birth_date": 1999,
        "Grades": (70, 75, 80)
    },
}

# 1. Kullanıcıdan numarayı al
students_no = int(input("Öğrenci no: "))

# 2. ÖNCE o numaraya ait öğrenciyi seçip bir değişkene atayalım (İşimiz kolaylaşır)
# Artık 'student' değişkeni sadece o kişinin bilgilerini tutuyor.
student = students[students_no]

print("İstenilen öğrencinin bilgileri: " + str(students[students_no]))
# Çıktı:
"""
> python uygulama-dictionary.py
    Öğrenci no: 310
    İstenilen öğrencinin bilgileri: {'Name': 'Christopher Chan', 'Surname': 'Bang', 'Birth_date': 1997, 'Grades': (75, 80, 75)}
"""

# 3. Ortalamayı Hesapla
# sum() toplar, len() kaç tane not olduğunu sayar.
average = sum(student["Grades"]) / len(student["Grades"])

# 4. Yaşı Hesapla (Şimdiki yıl 2025 kabul edildi)
age = 2025 - student["Birth_date"]

# 5. Yazdır
# student["Name"] diyerek doğrudan isme ulaşıyoruz, int() içine almaya gerek yok.
print(f"{students_no} numaralı {student['Name']} {student['Surname']} ismindeki öğrencinin yaşı {age} ve not ortalaması {average:.0f}.")
# Çıktı:
"""
> python uygulama-dictionary.py
    Öğrenci no: 310
    310 numaralı Christopher Chan Bang ismindeki öğrencinin yaşı 28 ve not ortalaması 77.
"""
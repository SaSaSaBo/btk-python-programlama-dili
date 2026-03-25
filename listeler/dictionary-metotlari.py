"""
          Metot           |                      Ne Yapar?
         .keys()          |         Sadece anahtarları (keys) liste olarak verir.
        .values()         |         Sadece değerleri (values) liste olarak verir.
         .items()         |         Hem anahtar hem değeri gruplar halinde verir.
          .get()          |     Anahtarı arar, yoksa hata vermez None döner (Güvenli erişim).
         .update()        |         Sözlüğe yeni veri ekler veya var olanı günceller.
         .clear()         |               Listedeki tüm elemanları siler.
         .copy()          |                 Linstenin kopyasını çıkarır.
         .pop()           |            Belirtilen index ile elemanı silinir.
        .popitem()        |             Eklenen son key-value değerini siler.
"""


# ------------------------ #

recipe = {
    "food_name": "Musakka",
    "foot_recipe": "tarif açıklaması",
    "image": "1.jpg"
}

outcome = recipe["food_name"]

print("Yemek adı: " + outcome)
# Çıktı:
"""
> python dictionary-metotlari.py
    Yemek adı: Musakka
"""

# ------------------------ #

outcome_get = recipe.get("food_name")

print("get metodu: " + outcome_get)
# Çıktı:
"""
> python dictionary-metotlari.py
    get metodu: Musakka
"""

# ------------------------ #

outcome_keys = recipe.keys()

print("keys metodu: " + str(outcome_keys))
# Çıktı:
"""
> python dictionary-metotlari.py
    keys metodu: dict_keys(['food_name', 'foot_recipe', 'image'])
"""

# ------------------------ #

outcome_values = recipe.values()

print("values metodu: " + str(outcome_values))
# Çıktı:
"""
> python dictionary-metotlari.py
    values metodu: dict_values(['Musakka', 'tarif açıklaması', '1.jpg'])
"""

# ------------------------ #

outcome_items = recipe.items()

print("items metodu: " + str(outcome_items))
# Çıktı:
"""
> python dictionary-metotlari.py
    items metodu: dict_items([('food_name', 'Musakka'), ('foot_recipe', 'tarif açıklaması'), ('image', '1.jpg')])
"""

# ------------------------ #

recipe["food_name2"] = "Mantı" # Eğer verilen key değeri yoksa ekleme yapar.

outcome_upgrade = recipe

print("Güncelleme: " + str(outcome_upgrade))
# Çıktı:
"""
> python dictionary-metotlari.py
   Güncelleme: {'food_name': 'Musakka', 'foot_recipe': 'tarif açıklaması', 'image': '1.jpg', 'food_name2': 'Mantı'}
"""

# ------------------------ #

recipe.update({"food_name": "Makarna"})
outcome_update = recipe

print("update metodu: " + str(outcome_update))
# Çıktı:
"""
> python dictionary-metotlari.py
   update metodu: {'food_name': 'Makarna', 'foot_recipe': 'tarif açıklaması', 'image': '1.jpg', 'food_name2': 'Mantı'}
"""

recipe.update({"food_name3": "Makarna"}) # Eğer verilen key değeri yoksa ekleme yapar.
outcome_update = recipe

print("update metodu: " + str(outcome_update))
# Çıktı:
"""
> python dictionary-metotlari.py
   update metodu: {'food_name': 'Makarna', 'foot_recipe': 'tarif açıklaması', 'image': '1.jpg', 'food_name2': 'Mantı', 'food_name3': 'Makarna'}
"""

# ------------------------ #

recipe.pop("food_name2")

print("pop metodu ile silinmiş hali: " + str(recipe))
# Çıktı:
"""
> python dictionary-metotlari.py
   pop metodu ile silinmiş hali: {'food_name': 'Makarna', 'foot_recipe': 'tarif açıklaması', 'image': '1.jpg', 'food_name3': 'Makarna'}
"""

# ------------------------ #

outcome_popitem = recipe.popitem()

print("popitem metodu ile silinmiş hali: " + str(recipe))
# Çıktı:
"""
> python dictionary-metotlari.py
   popitem metodu ile silinmiş hali: {'food_name': 'Makarna', 'foot_recipe': 'tarif açıklaması', 'image': '1.jpg'}
"""
# Przygotuj klasę o nazwie Restaurant. Metoda __init__() w klasie Restaurant powinna przechowywać dwa atrybuty:
# restaurant_name i cuisine_type. Utwórz metodę o nazwie describe_restaurant() wyświetlającą te dwa fragmenty informacji
# oraz metodę o nazwie open_restaurant() wyświetlającą informacje o godzinach pracy restauracji. Na podstawie
# przygotowanej klasy utwórz egzemplarz restaurant. Wyświetl oddzielnie oba atrybuty, a następnie wywołaj obie metody.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """opis restauracji"""
        print(f"Restauracja: {self.restaurant_name.title()}. W naszej ofercie jest kuchnia {self.cuisine_type}.")

    def open_restaurant(self):
        """godziny otwarcia"""
        print(f"Godziny otwarcia {self.restaurant_name.title()}: 16:00 - 22:00")

fav_restaurant = Restaurant("forsaken", "włoska")
print(f"Moja ulubiona restauracja to {fav_restaurant.restaurant_name.title()}.")
print(f"A ulubioną kuchnią jest ta, którą tam serwują czyli kuchnia {fav_restaurant.cuisine_type}.")
fav_restaurant.describe_restaurant()
fav_restaurant.open_restaurant()
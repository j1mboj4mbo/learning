# Pracę rozpocznij od klasy opracownej w ćwiczeniu 9.1. Utwórz trzy różne egzemplarze na podstawie tej klasy, a
# następnie wywołaj metodę describe_restaurant() dla każdego egzemplarza.
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

rest1 = Restaurant("Smakosz", "polska")
rest2 = Restaurant("Oh my Ramen", "japońska")
rest3 = Restaurant("Aroy Thai", "tajska")
rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()
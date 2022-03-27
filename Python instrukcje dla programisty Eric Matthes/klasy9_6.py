# Budka z lodami to szczególny rodzaj restauracji. Zdefiniuj klasę o nazwie IceCreamStand dziedziczącą po klasie
# Restaurant utworzonej w ćwiczeniu 9.1 lub 9.4. Dowolna wersja wymienionej klasy będzie się sprawdzać - po prostu
# wybierz jedną z nich. Dodaj atrybut o nazwie flavors, przechowujący listę różnych smaków lodów. Zdefiniuj metodę
# wyświetlającą dostępne smaki lodów. Utwórz egzemplarz klasy IceCreamStand i wywołaj nową metodę.

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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cousine_type):
        super().__init__(restaurant_name, cousine_type)
        self.flavors = ["czekoladowe", "waniliowe", "truskawkowe"]

    def show_flavors(self):
        print(f"Oto lista lodów:")
        for i in self.flavors:
            print(i)

ob1 = IceCreamStand("Lodziarnia u Paramaxila", "lodowa")
ob1.show_flavors()

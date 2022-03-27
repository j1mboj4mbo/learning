# Pracę rozpocznij od programu utworzonego w ćwiczeniu 9.1. Dodaj atrybut o nazwie number_served o wartości domyślnej 0.
# Następnie na podstawie klasy utwórz egzemplarz o nazwie restaurant. Wyświetl liczbę klientów obsłużonych przez
# restauracje, zmień tę wartość i później wyświetl nową.

# Dodaj metodę o nazwie set_number_served(), pozwalającą na zdefiniowanie liczby obsłużonych klientów. Wywołaj tę metodę
# wraz z różnymi wartościami i je wyświetl.

# Dodaj metodę o nazwie increment_number_served(), pozwalającą na inkrementację wartości wskazującej na liczbę
# obsłużonych klientów. Wywołaj tę metodę dowolną ilość razy, symulując w ten sposób liczbę klientów obsłużonych na
# przykład w ciągu dnia roboczego.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """opis restauracji"""
        print(f"Restauracja: {self.restaurant_name.title()}. W naszej ofercie jest kuchnia {self.cuisine_type}.")

    def open_restaurant(self):
        """godziny otwarcia"""
        print(f"Godziny otwarcia {self.restaurant_name.title()}: 16:00 - 22:00")

    def set_number_served(self):
        print(f"Liczba klientów: {self.number_served}")

    def increment_number_served(self, client):
        self.number_served += client


restaurant = Restaurant("Kebab Ostra Jazda", "kebab 🤙")
restaurant.number_served = 13
restaurant.set_number_served()
restaurant.increment_number_served(6)
restaurant.set_number_served()
restaurant.increment_number_served(12)
restaurant.set_number_served()
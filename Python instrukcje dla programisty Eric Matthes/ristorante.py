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
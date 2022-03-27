# Pracę rozpocznij od ostatniej wersji programu electric_car.py utworzonej w tym podrozdziale. Do klasy Battery dodaj
# nową metodę o nazwie upgrade_battery(). Ta metoda powinna sprawdzić pojemność akumulatora i ustawić ją na 100, jeśli
# aktualnie jest inna. Utwórz egzemplarz samochodu o napędzie elektrycznym wraz z akumulatorem o domyślnej pojemności,
# wywołaj metodę get_range(), a następnie metodę upgrade_battery() i ponownie get_range(). Powinieneś zauważyć
# zwiększenie zasięgu samochodu.

class Car():
    """Prosta próba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu.")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego."""

    def __init__(self, battery_size=75):
        """Inicjalizacja atrybutów akumulatora."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.")

    def get_range(self):
        """Wyświetla informacje o zasięgu samochodu na podstawie pojemności akumulatora"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Zasięg tego samochodu wynosi około {range} km po pełnym naładowaniu akumulatora.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów klasy nadrzędnej. Następnie inicjalizacja atryubtów charakterystycznych dla samochodu
         elektrycznego"""
        super().__init__(make, model, year)
        self.battery = Battery()

car = ElectricCar("tesla", "model s", 2019)
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
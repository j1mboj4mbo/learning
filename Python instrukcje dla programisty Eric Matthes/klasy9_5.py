# Pracę rozpocznij od programu utworzonego w ćwiczeniu 9.3. Do klasy User dodaj metodę o nazwie
# increment_login_attempts(), pozwalający na inkrementację wartości login_attempts o 1. Utwórz drugą metodę o nazwie
# reset_login_attempts(), która będzie zerowała wartość login_attempts.

# Utwórz egzemplarz klasy User i kilkukrotnie wywołaj metodę increment_login_attempts(). Wyświetl wartość
# login_attempts, aby mieć pewność o jej prawidłowej inkrementacji. Następnie wywołaj metodę reset_login_attempts().
# Ponownie wyświetl wartość login_attempts i sprawdź, czy na pewno wynosi 0.

class User():
    def __init__(self, first_name, last_name, age, country, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\nImię: {self.first_name.title()}")
        print(f"Nazwisko: {self.last_name.title()}")
        print(f"Wiek: {self.age.title()}")
        print(f"Kraj urodzenia: {self.country.title()}")

    def greet_user(self):
        print(f"Siema {self.first_name.title()}. Dobrze, że jesteś.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Jimbo", "Jambo", "21", "Poland")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Próby logowania: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Próby logowania: {user1.login_attempts}")
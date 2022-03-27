# Przygotuj klasę o nazwie User. Zdefiniuj w niej dwa atrybuty (first_name i last_name), a następne utwórz kilka innych
# atrybutów, które zwykle są przechowywane w profilu użytkownika. Zdefiniuj metodę o nazwie describe_user()
# wyświetlającą podsumowanie informacji zebranych o użytkowniku. Utwórz jeszcze drugą metodę o nazwie greet_user(), która
# będzie wyświetlała użytkownikowi spersonalizowane powitanie.

# Utwórz kilka egzemplarzy reprezentujących różnych użytkowników, a następnie dla każdego z nich wywołaj obie metody.

class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"\nImię: {self.first_name.title()}")
        print(f"Nazwisko: {self.last_name.title()}")
        print(f"Wiek: {self.age.title()}")
        print(f"Kraj urodzenia: {self.country.title()}")

    def greet_user(self):
        print(f"Siema {self.first_name.title()}. Dobrze, że jesteś. xd")

user1 = User("Gabriel", "Pankała", "21", "Polska")
user2 = User("Artur", "Janduda", "21", "Polska")
user3 = User("Patryk", "Brzoska", "?", "Turcja")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
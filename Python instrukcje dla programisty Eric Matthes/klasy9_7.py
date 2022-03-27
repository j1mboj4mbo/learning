# Administrator to specjalny rodzaj użytkownika. Zdefiniuj klasę o nazwie Admin dziedziczącą po klasie User utworzonej
# w ćwiczeniu 9.3 lub 9.5. Dodaj atrybut privileges przechowujący listę ciągów tekstowych takich jak "może dodać post",
# "może usunąć post" czy "może zbanować użytkownika". Zdefiniuj metodę o nazwie show_privileges(), wyświetlającą listę
# uprawnień administratora. Utwórz egzemplarz klasy Admin i wywołaj nową metodę.
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

class Admin(User):
    def __init__(self, first_name, last_name, age, country, login_attempts=0):
        super().__init__(first_name, last_name, age, country, login_attempts)
        self.privileges = ["może dodać post", "może usunąć post", "może zbanować użytkownika"]

    def show_privileges(self):
        print(f"Uprawnienia {self.first_name.title()} {self.last_name.title()}:")
        for i in self.privileges:
            print(i)

admin = Admin("Jimbo", "Jambo", 21, "Poland")
admin.show_privileges()
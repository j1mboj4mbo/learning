# Zdefiniuj oddzielną klasę Privileges. Ta klasa powinna mieć jeden atrybut(privileges), przechowujący listę ciągów
# tekstowych, tak jak przedstawiłem to w poprzednim ćwiczeniu. Metodę show_privileges() przenieś do nowej klasy. Utwórz
# egzemplarz klasy Privileges jako atrybut w klasie Admin. Następnie utwórz nowy egzemplarz klasy Admin i użyj metody
# show_privileges() do wyświetlenia uprawnień.

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

class Privileges():

    def __init__(self):
        self.privileges = ["może dodać post", "może usunąć post", "może zbanować użytkownika"]

    def show_privileges(self):
        print(f"Uprawnienia:")
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name, last_name, age, country, login_attempts=0):
        super().__init__(first_name, last_name, age, country, login_attempts)
        self.privileges = Privileges()

# user1 = Admin("Jimbo", "Jambo", 21, "Poland")
# user1.privileges.show_privileges()
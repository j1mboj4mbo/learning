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
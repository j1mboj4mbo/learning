import userhelp as uh
class Privileges():

    def __init__(self):
        self.privileges = ["może dodać post", "może usunąć post", "może zbanować użytkownika"]

    def show_privileges(self):
        print(f"Uprawnienia:")
        for i in self.privileges:
            print(i)

class Admin(uh.User):
    def __init__(self, first_name, last_name, age, country, login_attempts=0):
        super().__init__(first_name, last_name, age, country, login_attempts)
        self.privileges = Privileges()
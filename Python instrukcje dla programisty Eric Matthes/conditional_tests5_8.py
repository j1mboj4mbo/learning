current_users = ["admin", "eryk", "arczi", "lajert"]
new_users = ["eryk", "lolo", "test"]
login1 = "eryk"

for x in new_users:
    if(x in current_users):
        print(f'Nazwa użytkownika "{x}" nie może zostać użyta, spróbuj innej.')
    else:
        print(f'Nazwa użytkownika "{x}" może zostać użyta.')

if current_users:
    if login1.lower() == "admin":
        print(f"Witaj {login1.title()}. Czy chcesz przejrzeć dzisiejsze raporty?")
    elif login1.lower() in current_users:
        print(f"Witaj {login1.title()}. Dziękujemy za ponowne logowanie.")
    else:
        print(f"Błędna nazwa użytkownika.")
else:
    print("Powinniśmy dodać kilku pracowników.")
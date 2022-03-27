# W ostatniej wersji programu remember_me.py przyjęto założenie, że użytkownik już wcześniej podał swoje imię lub też
# program został uruchomiony po raz pierwszy. Powinniśmy zmodyfikować ten program na wypadek, gdyby bieżący użytkownik
# nie był tą osobą, która ostatnio korzystała z tego programu.
# W funkcji greet_user(), zanim za pomocą odpowiedniego komunikatu powitasz istniejącego już użytkownika, zapytaj go,
# czy podane imię jest poprawne. Jeżeli nie jest, należy wywołać funkcję get_new_username() w celu użycia prawidłowego
# imienia.
import json

def get_stored_username():
    """Pobranie imienia z pliku, o ile taki istnieje."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Poproszenie użytkownika, aby podał swoje imię, a następnie zapisanie tego imienia w pliku."""
    username = input("Podaj swoje imię: ")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    username = get_stored_username()
    if username:
        print(f"Jesteś {username}? (T/N):")
        question = input("").lower()
        if question == "n":
            username = get_new_username()
            print(f"Twoje imię zostało zapisane i będzie używane później {username}.")
    else:
        username = get_new_username()
        print(f"Twoje imię zostało zapisane i będzie używane później {username}.")

greet_user()
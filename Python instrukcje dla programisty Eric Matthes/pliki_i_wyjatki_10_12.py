# Oba programy utworzone w poprzednim ćwiczeniu połącz w jednym pliku. Jeżeli ulubiona liczba została zapisana w pliku,
# wyświetl ją użytkownikowi. W przeciwnym razie poproś użytkownika o podanie ulubionej liczby i zapisz ją w pliku.
# Uruchom ten program dwukrotnie i upewnij się, że działa prawidłowo.
import json

filename = "favourite_number2.json"
try:
    with open(filename) as f:
        fav = json.load(f)
except FileNotFoundError:
    fav_number = input("Podaj swoją ulubioną liczbę: ")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
else:
    print(f"Twoja ulubiona liczba to {fav}.")
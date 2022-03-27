# Utwórz program, który prosi użytkownika o podanie ulubionej liczby. Za pomocą funkcji json.dump() zapisz tę liczbę w
# pliku. Następnie utwórz oddzielny program odczytujący ulubioną liczbę użytkownika i wyświetlający komunikat w stylu:
# "Znam Twoją ulubioną liczbę, to ..."
import json
fav_number = input("Podaj swoją ulubioną liczbę: ")
filename = "favourite_number.json"
with open(filename, 'w') as f:
    json.dump(fav_number, f)

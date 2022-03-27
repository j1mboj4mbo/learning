# Utwórz listę lub krotkę zawierającą serię dziesięciu liczb i pięciu liter. Losowo wybierz cztery liczby lub litery z
# listy, a następnie wyświetl komunikat informujący, że kupon zawierający liczby lub litery dopasowane do wylosowanych
# wygrywa nagrodę.
from random import choice
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]
print("Wygrywające liczby to:")
for x in range(4):
    print(choice(list))


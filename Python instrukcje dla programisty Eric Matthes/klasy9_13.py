# Przygotuj klasę Die z jednym atrybutem o nazwie sides, którego wartośćią domyślną będzie 6. Utwórz metodę o nazwie
# roll_die(), wyświetlającą losowo wygenerowaną liczbę z zakresu od 1 do wartości określonej przez liczbę ścianek na
# kości do gry. Utwórz kość zawierającą sześć scianek i zasymuluj rzucenie nią 10 razy.
# Później utwórz kości zawierające 10 i 20 ścianek. Każdą nową kością rzuć 10 razy.
import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        rolling = random.randint(1, self.sides)
        print(f"Wyrzucono {rolling}")

die = Die(20)
for i in range(10):
    die.roll_die()


# Wykorzystaj pętle do ustalenia, jak trudno jest wygrać w loterii, którą modelowałeś w poprzednim ćwiczeniu. Utwórz
# listę lub krotkę o nazwie my_ticket. Następnie zdefiniuj pętle losującą liczby dopóty, dopóki nie zostaną dopasowane
# do Twojego kuponu. Wyświetl komunikat informujący, ile iteracji pętli trzeba było wykonać, zanim padły liczby
# znajdujące się na Twoim kuponie.
from random import choice
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]
my_ticket = "C"
list2 = []
close = True
while(close):
    test = choice(list)
    list2.append(test)
    print(test)
    if test == my_ticket:
        close = False
print(list2)
print(f"Trzeba było wykonać {len(list2)} pętli żeby wylosować {my_ticket}")

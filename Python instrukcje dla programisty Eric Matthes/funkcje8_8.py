# Pracę rozpocznij od programu utworzonego w ćwiczeniu 8.7. Dodaj pętlę while pozwalającą użytkownikom na wprowadzenie
# artysty i tytułu płyty. Po zebraniu tych informacji wywołaj funkcję make_album() wraz z podanymi przez użytkownika
# danymi wejściowymi oraz wyświetl słownik utworzony przez program. Upewnij się, że zdefiniowałeś wartość pozwalającą
# opuścić pętlę while.
def make_album(name, title):
    album = {"nazwa": name, "tytuł": title}
    formatted = f"Nazwa: {album['nazwa'].title()}, Tytuł: {album['tytuł'].title()}"
    return formatted
while(True):
    print("\nPodaj nazwę oraz tytuł albumu.")
    print('Wpisz "q" w dowolnym momencie by przerwać działanie programu')
    name = input("Nazwa artysty/zespołu: ")
    if name == "q":
        break
    title = input("Tytuł albumu: ")
    if title == "q":
        break

    print(make_album(name, title))
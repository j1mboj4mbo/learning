# Utwórz funkcję o nazwie make_album() odpowiedzialną za zbudowanie słownika reprezentującego album muzyczny.
# Funkcja powinna pobrać nazwę zespołu lub artysty oraz tytuł albumu. Wartością zwrotną funkcji powinien być słownik
# zawierający te dwa fragmenty informacji. Za pomocą przygotowanej funkcji utwórz trzy słowniki przedstawiające różne
# albumy. Wyświetl każdą wartość zwrotną, aby pokazać, że słowniki prawidłowo przechowują informacj o albumach.
# Wykorzystując wartość specjalną None, do funkcji make_album() dodaj opcjonalny parametr pozwalający na przechowywanie
# liczby utworów znajdujących się na płycie. Jeżeli wywołanie funkcji będzie zawierało wartość dla liczby utworów,
# należy ją dodać do słownika informacji o albumie. Zdefiniuj co najmniej jedno nowe wywołanie funkcji obejmujące także
# liczbę utworów na płycie.
def make_album(name, title, songs=None):
    album = {"nazwa": name, "tytuł": title}
    if songs:
        album["liczba utworów"] = songs
    return album
print(make_album("Quebonafide", "Egzotyka", 15))
print(make_album("Taco Hemingway", "Marmur"))
print(make_album("Taconafide", "SOMA 0.5mg"))
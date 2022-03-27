# Jeden z najcześciej pojawiających się problemów podczas pobierania danych liczbowych polega na tym, że użytkownicy
# podają tekst zamiast liczb. Kiedy tego rodzaju dane wejściowe spróbujesz skonwertować na typ int, otrzymasz błąd
# ValueError. Utwórz program, który prosi użytkownika o podanie dwóch liczb. Dodaj je i wyświetl wynik. Przechwyć błąd
# ValueError, jeżeli którakolwiek wartość przekazana w danych wejściowych nie jest liczbą, i wyświetl odpowiedni
# komunikat błędu. Przetestuj program, najpierw podając dwie liczby, a później pewien tekst zamiast liczby.
# while(True):
try:
    int1 = int(input("Podaj 1 liczbę: "))
    int2 = int(input("Podaj 2 liczbę: "))
    print(f"Suma: {int1 + int2}")
    # break
except ValueError:
    print("//wprowadzono literę zamiast liczby//")
    # continue


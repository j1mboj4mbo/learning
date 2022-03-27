# Kod przygotowany w ćwiczeniu 10.6 opakuj pętlą while, aby użytkownik mógł kontynuować wprowadzenie liczb nawet po
# popełnieniu błędu i podaniu tekstu zamiast liczby.
while(True):
    try:
        int1 = int(input("Podaj 1 liczbę: "))
        int2 = int(input("Podaj 2 liczbę: "))
        print(f"Suma: {int1 + int2}")
        break
    except ValueError:
        print("//wprowadzono literę zamiast liczby//")
        continue

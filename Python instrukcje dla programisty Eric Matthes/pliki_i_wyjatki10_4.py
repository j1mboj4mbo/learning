# Utwórz pętle while, w której każdy użytkownik będzie musiał podać swoje imię. Gdy użytkownik je wprowadzi, na ekranie
# wyświetl komunikat powitania, a do pliku o nazwie guest_book.txt dodaj wiersz rejestrujący odwiedzenie Twojej strony
# przez tego użytkownika. Upewnij się, że każdy wpis jest umieszczany w nowym wierszu w pliku.
end = True
with open("guest_book.txt", 'a') as f:
    while(end):
        text = input("Podaj swoje imię (napisz 'koniec' by zakończyć działanie programu': ")
        if text == 'koniec':
            end = False
            print("Zakończenie działania programu.")
        else:
            print(f"Witaj {text}!")
            f.write(f"{text}\n")
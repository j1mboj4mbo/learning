# Utwórz program, który poprosi użytkownika o podanie imienia. Gdy użytkownik je wprowadzi, zapisz to imię w pliku o
# nazwie guest.txt
with open("guest.txt", 'a') as f:
    text = input("Podaj imię: ")
    f.write(f"{text}\n")
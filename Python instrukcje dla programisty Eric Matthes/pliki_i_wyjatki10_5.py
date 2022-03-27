# Utwórz pętlę while, w której użytkownicy będą musieli udzielić odpowiedzi na pytanie: "Dlaczego lubisz programowanie?"
# Każdą otrzymaną odpowiedź dodaj do pliku przechowującego wszystkie udzielone odpowiedzi.
with open("answers.txt", 'a') as f:
    close = True
    while(close):
        question = input("Dlaczego lubisz programowanie? (napisz 'koniec' by zakończyć działanie programu): ")
        if question == "koniec":
            close = False
            print("Zakończenie działania programu.")
        else:
            f.write(f"{question}\n")
            print("Dziękuję za odpowiedź.")

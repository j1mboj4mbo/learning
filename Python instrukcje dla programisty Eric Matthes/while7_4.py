msg = "Podaj składniki."
msg += "\nNapisz 'koniec', aby zakończyć działanie programu. "
mess = ""
while mess != 'koniec':
    mess = input(msg)
    print(f"Pomyślnie dodano {mess} do zamówienia.")

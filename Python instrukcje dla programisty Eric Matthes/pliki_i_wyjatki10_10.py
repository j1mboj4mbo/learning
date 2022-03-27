# Wybierz kilka innych książek, które chciałyś przeanalizować. Pobierz pliki tekstowe tych dzieł lub niezmodyfikowany
# zwykły tekst skopiuj z przeglądarki internetowej do pliku tekstowego w komputerze. Za pomocą metody count() możesz
# sprawdzić, ile razy dane słowo lub wyrażenie występuje w ciągu tekstowym. Na przykłąd w przedstawionym poniżej
# fragmencie kodu sprawdzamy, ile razy słowo za występuje w ciągu tekstowym.
# line = "Za górami, za lasami, za dolinami pobili się dwaj górale ciupagami"
# line.count('za')
# 2
# line.lower().count('za')
# 3
# Zwróć uwagę na to, że konwersja ciągu tekstowe na zapisany małymi literami powoduje przechwycenie wszystkich wystąpień
# sprawdzanego słowa niezależnie od sposobu jego formatowania.
# Utwórz program odczytujący pobrane wcześniej z projektu Gutenberg pliki tekstowe, a następnie określający ile razy,
# słowo 'the' występuje w każdym z nich. Otrzymany wynik będzie jedynie przybliżony, ponieważ uwzględnia również słowa
# zawierające 'za', np. 'zachód' lub 'zabawa'. Spróbuj zliczyć wystąpienie 'za '(wraz ze spacją w ciągu tekstowym) i
# zobacz, o ile mniejsza będzie to liczba.

def counting(filename):
    try:
        with open(filename, encoding='utf8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje.")
    else:
        words = text.split()
        print(f"Plik '{filename}' ma {len(words)} słów.")

def the_counting(filename):
    try:
        with open(filename, encoding='utf8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje.")
    else:
        print(f'Słowo "the" występuje w pliku "{filename}" {text.lower().count("the ")} razy.\n')

filenames = ['rocks_and_their_origins.txt', 'some_problems_of_the_peace_conference.txt', 'trans.txt.']
for filename in filenames:
    counting(filename)
    the_counting(filename)

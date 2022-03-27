# Metodę replace() można wykorzystać do zastąpienia dowolnego słowa w ciągu tekstowym zupełnie innym słowem. Oto krótki
# przykład pokazujący jak w zdaniu słowo pies zastąpić słowem kot.
# message = "Moje ulubione zwierzę to pies."
# message.replace('pies', 'kot')
# "Moje ulubione zwierzę to kot."
# Odczytaj każdy wiersz tekstu w utworzonym wcześniej pliku learning_python.txt, a następnie wszystkie wystąpienia słowa
# Python zastąp nazwą innego języka programowania, na przykład C. Każdy zmodyfikowany wiersz wyświetl na ekranie.
with open('learning_python.txt', encoding='utf8') as f:
    for i in f:
        message = i.replace('Pythonie', 'Java')
        print(message.strip())

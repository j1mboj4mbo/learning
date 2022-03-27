# W edytorze tekstu utwórz pusty plik i wpisz w nim kilka zdań podsumowujących to, czego się dotąd nauczyłeś o języku
# Python. Każdy wiersz rozpocznij od wyrażenia "w Pythonie można...". Plik zapisz pod nazwą learning_python.txt w tym
# samym katologu, w którym umieszczasz ćwiczenia z tego rozdziału. Przygotuj program odczytujący powyższy plik i
# trzykrotnie wyświetlający jego zawartość. Treść pliku powinna być wyświetlona raz przez odczytanie całego pliku, raz
# za pomocą iteracji przez obiekt pliku oraz raz przez umieszczenie wierszy na liście, a następnie przetworzenie listy
# poza blokiem with.
file = 'learning_python.txt'
list = []

with open(file, encoding='utf8') as file_object:
    for line in file_object:
        print(line.strip())
#
with open(file, encoding='utf8') as file_object:
    print(f'\n{file_object.read()}')

with open(file, encoding='utf8') as file_object:
    list.append(file_object.read())

for i in list:
    print(i)
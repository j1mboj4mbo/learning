# Utwórz dwa pliki o nazwach cats.txt i dogs.txt. W pierwszym pliku umieść przynajmniej trzy imiona kotów, natomiast w
# drugim przynajmniej trzy imiona psów. Przygotuj program próbujący odczytać zawartość tych plików i wyświetlić ją na
# ekranie. Zastosuj w kodzie: konstrukcję try-except, aby przechwycić wszelkie błędy typu FileNotFoundError i wyświetlić
# użytkownikowi odpowiedni komunikat błędu, gdy zażądany plik nie istnieje. Jeden z utworzonych wcześniej plików
# przenieś do innego katalogu w systemie i upewnij się, że opracowany blok except w programie działa prawidłowo.
filenames = ['dogs.txt', 'cats.txt', 'rats.txt']
for filename in filenames:
    try:
        with open(filename, encoding='utf8') as f:
            print(f.read().strip())
            print("")
    except FileNotFoundError:
        print(f"Plik {filename} nie znajduje się w folderze z programem.")
        
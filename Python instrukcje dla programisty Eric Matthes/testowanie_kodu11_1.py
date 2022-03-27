# Przygotuj funkcję akceptującą dwa parametry: nazwy miasta i państwa. Wartością zwortną tej funkcji powinien być
# pojedyńczy ciąg tekstowy w postaci Miasto, Państwo, na przykład Santiago, Chile. Gotową funkcję umieść w module o
# nazwie city_functions.py.
# Utwórz plik o nazwie test_cities.py przeznaczony do przetestowania przygotowanej wcześniej funkcji (pamiętaj o
# konieczności zaimportowania modułu unittest oraz funkcji, która ma zostać sprawdzona). Następnie w pliku
# test_cities.py zdefiniuj funkcję o nazwie test_city_country() odpowiedialną za sprawdzenie, czy wywołanie utworzonej
# w poprzednim ćwiczeniu funkcji, na przykład z wartościami 'santiago' i 'chile', spowoduje wygenerowanie oczekiwanego
# ciągu tekstowego. Uruchom plik test_cities.py i upewnij się, że test test_city_country() zostaje zaliczony.
def get_city_functions(city, country, population=''):
    """Zwrot 'Miasto, Państwo'"""
    if population:
        city_country = f"{city.title()}, {country.title()}, populacja - {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country

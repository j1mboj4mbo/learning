# Przygotuj funkcję akceptującą dwa parametry: nazwy miasta i państwa. Wartością zwortną tej funkcji powinien być
# pojedyńczy ciąg tekstowy w postaci Miasto, Państwo, na przykład Santiago, Chile. Gotową funkcję umieść w module o
# nazwie city_functions.py.
# Utwórz plik o nazwie test_cities.py przeznaczony do przetestowania przygotowanej wcześniej funkcji (pamiętaj o
# konieczności zaimportowania modułu unittest oraz funkcji, która ma zostać sprawdzona). Następnie w pliku
# test_cities.py zdefiniuj funkcję o nazwie test_city_country() odpowiedialną za sprawdzenie, czy wywołanie utworzonej
# w poprzednim ćwiczeniu funkcji, na przykład z wartościami 'santiago' i 'chile', spowoduje wygenerowanie oczekiwanego
# ciągu tekstowego. Uruchom plik test_cities.py i upewnij się, że test test_city_country() zostaje zaliczony.

# Zmodyfikuj przygotowaną wcześniej funkcję, aby wymagała podania trzeciego argumentu - populacji(population). Teraz
# wartością zwrotną funkcji powinien być ciąg tekstowy w postaci Miasto, Państwo - populacja xxx, na przykład Santiago
# Chile - populacja 5000000. Ponownie uruchom test_cities.py. Upewnij się, że tym razem test zdefiniowany w metodzie
# test_cities_country() będzie niezaliczony.
# Zmodyfikuj funkcję, aby parametr population był opcjonalny. Ponownie uruchom test_cities.py. Upewnij się, że tym razem
# test zdefiniowany w metodzie test_city_country() zostanie zaliczony.
# Utwórz drugi test o nazwie test_city_country_population(), sprawdzający, czy można wywołać funkcję z wartościami
# 'santiago', 'chile' i 'population=5000000'. Raz jeszcze uruchom test_cities.py i upewnij się, że nowy test został
# zaliczony.
import unittest
from testowanie_kodu11_1 import get_city_functions


class NamesTestCase(unittest.TestCase):

    """Test dla city_functions / testowanie_kodu_11_1"""
    def test_city_country(self):
        formatted_name = get_city_functions('madrid', "spain")
        self.assertEqual(formatted_name, "Madrid, Spain")

    def test_city_country_population(self):
        name = get_city_functions('santiago', 'chile', '5000000')
        self.assertEqual(name, "Santiago, Chile, populacja - 5000000")


if __name__ == '__main__':
    unittest.main()

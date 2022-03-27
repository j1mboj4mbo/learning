# Utwórz funkcję przechowującą w słowniku informacje o samochodzie. Ta funkcja zawsze powinna otrzymywać nazwy marki i
# modelu pojazdu, po którym można podać dowolną liczbę argumentów w postaci słów kluczowych. Wywołaj funkcję zawierającą
# wymagane informacje oraz dwie dodatkowe pary nazwa-wartość, na przykład opisujące kolor i wyposażenie dodatkowe.
# Przygotowana funkcja powinna być wywoływana w sposób podobny do przedstawionego poniżej:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Wyświetl zawartość słownika zwróconego przez tą funkcję i upewnij się, że wszystkie podane informacje zostały w nim
# prawidłowo zapisane.
def make_car(brand, model, **car_info):
    car_info['brand'] = brand
    car_info['model'] = model
    return car_info

car = make_car('bmw', 'm5', color='white', additional_information='ac')
print(car)

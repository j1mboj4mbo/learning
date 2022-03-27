# Utwórz funkcję o nazwie city_country() pobierającą nazwę miasta i kraju, w którym ono leży. Wartością zwrotną funkcji
# powinien być ciąg tekstowy sformatowany w poniższy sposób:
# Santiago, Chile
# Przygotowaną funkcję wywołaj z przynajmniej trzema parami miasto-państwo i wyświetl wygenerowaną przez nie wartość.
def city_country(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()
print(city_country("warsaw", "poland"))
print(city_country("paris", "france"))
print(city_country("berlin", "germany"))

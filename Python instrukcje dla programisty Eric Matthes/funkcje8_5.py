# Utwórz funkcję o nazwie describe_city(), akceptującą nazwę miasta i kraju. Ta funkcja powinna wyświetlać proste
# zdanie, takie jak "Warszawa leży w Polsce". Parametrowi przechowującemu nazwę państwa przypisz wartość domyślną.
# Przygotowaną funkcję wywołaj dla trzech różnych miast, z których przynajmniej jedno nie powinno być położone w
# domyślnie zdefiniowanym kraju.
def describe_city(city, country="Polsce"):
    print(f"{city} leży w {country}")
describe_city(city="Kraków")
describe_city(city="Warszawa")
describe_city(city="Paryż", country="Francji")
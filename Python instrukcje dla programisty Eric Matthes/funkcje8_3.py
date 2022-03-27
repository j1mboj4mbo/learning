# Utwórz funkcję o nazwie make_shirt(), akceptującą wielkość koszulki oraz tekst, który ma zostać na niej nadrukowany.
# Funkcja powinna wyświetlić zdanie zawierające informacje dotyczące zamówionej koszulki: jej rozmiar i tekst do
# wydrukowania na niej.
# W trakcie pierwszego wywołania funkcji do przygotowania koszulki zastosuj argumenty pozycyjne.
# Natomiast w trakcie drugiego wywołania użyj argumentów w postaci słów kluczowych.
def make_shirt(size, text):
    print(f"Rozmiar zamówionej koszulki {size}. Tekst na koszulce: {text}")
make_shirt("M", "PROSTO")
make_shirt(text="abibas", size="XXL")

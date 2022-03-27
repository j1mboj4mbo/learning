# Utwórz funkcję akceptującą listę składników, które klient chce umieścić w zamawianej kanapce. Funkcja powinna zawierać
# jeden parametr przechowujący dowolną liczbę argumentów przekazanych w wywołaniu funkcji oraz wyświetlać podsumowanie
# dotyczące zamówionej kanapki. Przygotowaną funkcję wywołaj trzykrotnie, za każdym razem z inną liczbą argumentów.
def make_sandwich(*toppings):
    print("\nPrzygotowanie kanapki ze składnikami:")
    for topping in toppings:
        print(topping)
make_sandwich("szynka", "ser")
make_sandwich("sałata", "pomidor", "ogórek")
make_sandwich("tuńczyk")

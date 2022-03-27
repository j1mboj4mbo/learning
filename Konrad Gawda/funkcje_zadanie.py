def dodaj_wydruki(f):
    def wrapper(n):
        print("Start funkcji")
        result = f(n)
        print(f"Koniec funkcji")
        return result
    return wrapper

def kwadrat(x):
    print("Liczę kwadrat z", x)
    return x ** 2

# kwadrat_z_wydrukami = dodaj_wydruki(kwadrat)
# rezultat = kwadrat_z_wydrukami(2)
# assert rezultat == 4

@dodaj_wydruki
# @dodaj_wydruki przed definicją funkcji znaczy to samo co po definicji zrobienie:
# szescian = dodaj_wydruki(szescian)
def szescian(x):
    print("Liczę sześcian z", x)
    return x ** 3

print(szescian(6))

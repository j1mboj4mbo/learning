# Wykorzystaj utworzony przez siebie program z jedną funkcją i przenieś ją do oddzielnego pliku. Zaimportuj tę funkcję
# w pliku programu głównego, a następnie wywołaj funkcję na wszystkie wymienione poniżej sposoby:
# import nazwa_modułu
# from nazwa_modułu import nazwa_funkcji
# from nazwa_modułu import nazwa_funkcji as fn
# import nazwa_modułu as mn
# from nazwa_modułu import *
from car_making_function import *

print(make_car("audi", "a3", color="green"))
# Funkcję z programu print_models.py umieść w oddzielnym pliku o nazwie printing_functions.py. Na początku pliku
# print_models.py umieść polecenie import i zmodyfikuj plik w taki sposób, aby używać zaimportowanych funkcji.
import printing_functions as pf
unprinted_designs = ["test", "test3", "cos"]
completed_models = []
pf.print_models(unprinted_designs, completed_models)

# Przygotuj listę o nazwie sandwich_orders i umieść na niej nazwy różnych kanapek.
# Następnie przygotuj pustą listę o nazwie finished_sandwiches.
# Przeprowadź iterację przez listę zamówionych kanapek i wyświetl informację o danym zamówieniu, na przykład:
# "Przygotowano kanapkę z tuńczykiem". Kiedy kanapka zostanie zrobiona, reprezentujący ją element powinien zostać
# przeniesiony na listę finished_sandwiches. Gdy lista sadwich_orders będzie już pusta, wyświetl komunikat zawierający
# listę wszystkich wszystkich zrobionych kanapek.
sandwich_orders = ["kanapka z masłem", "kanapka z serem", "kanapka z serem i szynką", "chlyb z tustym"]
finished_sandwiches = []
while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f"Przygotowano {finished}.")
    finished_sandwiches.append(finished)
print(f"Łącznie przygotowane kanapki:")
for i in finished_sandwiches:
    print(i)
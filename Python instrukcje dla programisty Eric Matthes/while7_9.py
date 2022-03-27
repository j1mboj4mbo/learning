# Brak pastrami. Wykorzystaj listę sandwich_orders z ćwiczenia 7.8 i upewnij się, że na liście przynajmniej trzykrotnie
# pojawia się kanapka z pastrami. Gdzieś na początku programu umieść kod wyświetlający komunikat, że w barze skończyło
# się pastrami, a następnie za pomocą pętli while usuń wszystkie wystąpienia pastrami z listy sandwich_orders. Upewnij
# się, że żadna kanapka z pastrami nie zostanie umieszczona na liście finished_sandwiches.
sandwich_orders = ["kanapka z masłem", "pastrami", "kanapka z serem", "pastrami", "kanapka z serem i szynką",
                   "pastrami", "chlyb z tustym"]
finished_sandwiches = []
print("Przepraszamy, pastrami skończyło się.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    finish = sandwich_orders.pop()
    finished_sandwiches.append(finish)
print(finished_sandwiches)
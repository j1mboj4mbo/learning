# Przygotuj listę zawierającą serię krótkich komunikatów, a następnie przekaż ją do funkcji o nazwie show_messages(),
# która powinna wyświetlić każdy komunikat umieszczony na tej liście.
def show_messages(list):
    for message in list:
        print(message)
list = ["buy bp hmm", "buy bp uh", "buy point scroll", "sell bp gfb", "sell premium scroll"]
show_messages(list)
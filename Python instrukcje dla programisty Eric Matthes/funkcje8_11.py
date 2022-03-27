# Pracę rozpocznij od kodu utworzonego w ćwiczeniu 8.10. Wywołaj funkcję send_messages() wraz z kopią listy komunikatów.
# Po wywołaniu funkcji wyświetl obie listy, aby pokazać istnienie pierwotnej listy z zachowanymi komunikatami.
def show_messages(list, sent_messages):
    while list:
        current_message = list.pop()
        print(f"Advert: {current_message}")
        sent_messages.append(current_message)

def send_messages(sent_messages):
    print("List of current adverts:")
    for msg in sent_messages:
        print(msg)

list_messages = ["buy bp hmm", "buy bp uh", "buy point scroll", "sell bp gfb", "sell premium scroll"]
sent_messages = []
show_messages(list_messages[:], sent_messages)
send_messages(sent_messages)
print(list_messages)
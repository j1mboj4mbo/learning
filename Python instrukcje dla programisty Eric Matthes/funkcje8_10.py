# Pracę rozpocznij od kopii programu z ćwiczenia 8.9. Następnie utwórz funkcję o nazwie send_messages(), której zadaniem
# będzie wyświetlenie wszystkich komunikatów, a następnie przeniesienie ich na nową listę o nazwie sent_messages. Po
# wywołaniu funkcji należy wyświetlić obie listy i upewnić się o prawidłowym przeniesieniu komunikatów.
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
show_messages(list_messages, sent_messages)
send_messages(sent_messages)
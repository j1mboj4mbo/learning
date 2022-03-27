# Przygotuj program pytający użytkowników o ich wymarzone wakacje. Program powinien wyświetlać pytanie w stylu: "Jeżeli
# mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał?" Umieść w programie blok kodu odpowiedzialny
# za wyświetlenie wyników przeprowadzonej ankiety."
baza = {}
active = True
while active:
    name = input("Podaj swoje imię: ")
    place = input("Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał?: ")
    question = input("Dziękujemy za udział w ankiecie. Czy inny użytkownik chce udzielić odpowiedzi? T/N ").upper()
    baza[name] = place
    if question == "N":
        active = False
print("Wyniki ankiety:")
for name, place in baza.items():
    print(f"{name.title()} chce odwiedzić {place.title()}.")
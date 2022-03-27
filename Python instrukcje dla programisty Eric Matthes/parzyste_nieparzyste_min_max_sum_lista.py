# list = [] #tworzenie pustej listy
# for i in range(1, 1000001): #pętla dla wartości od 1 do 1000000 (zawsze o jeden więcej)
#     list.append(i) #dodanie wartości i do listy
# print(list) #pokazanie listy
# print(min(list)) #pokazanie minimalnej liczby z listy
# print(max(list)) #pokazanie maksymalnej liczby z listy
# print(sum(list)) #pokazanie sumy każdej liczby z listy

# 4.10

# list = [value**3 for value in range (1,10)]
# print(f"Pierwsze trzy elementy listy to: {list[:3]}")
# print(f"Środkowe trzy elementy listy to: {list[3:6]}")
# print(f"Pierwsze trzy elementy listy to: {list[-3:]}")

# 4.11

pizzas = ["wiejska", "diavolo", "4 sery"]
friend_pizzas = pizzas[:]
pizzas.append("margharitta")
friend_pizzas.append("frutti di mare")
print("Moja ulubiona pizza to:")
for pizza in pizzas:
    print(pizza)
print("Ulubiona pizza mojego kolegi to:")
for pizza in friend_pizzas:
    print(pizza)

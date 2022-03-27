import json
filename = 'favourite_number.json'
with open(filename) as f:
    fav = json.load(f)
print(f"Twoja ulubiona liczba to {fav}.")
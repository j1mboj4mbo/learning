dolphin = {'nazwa': 'delfin', 'gatunek': 'ssak'}
frog = {'nazwa': 'żaba', 'gatunek': 'płaz'}
snake = {'nazwa': 'wąż', 'gatunek': 'gad'}
butterfly = {'nazwa': 'motyl', 'gatunek': 'owad'}
pets = [dolphin, frog, snake, butterfly]
for x in pets:
    print(f"Nazwa: {x['nazwa'].title()}, Gatunek: {x['gatunek'].title()}")
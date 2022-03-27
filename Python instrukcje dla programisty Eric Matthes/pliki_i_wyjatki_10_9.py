# Blok except w programie utworzonym w poprzednim ćwiczeniu zmodyfikuj w taki sposób, aby brak pliku powodował jedynie
# ciche niepowodzenie.
filenames = ['dogs.txt', 'cats.txt', 'rats.txt']
for filename in filenames:
    try:
        with open(filename, encoding='utf8') as f:
            print(f.read().strip())
            print("")
    except FileNotFoundError:
        pass

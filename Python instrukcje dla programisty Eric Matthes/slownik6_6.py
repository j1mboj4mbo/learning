favourite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
    }
print(f"W ankiecie wzięli udział:")
for l in favourite_languages.keys():
    print(f"{l.title()}, dziękujemy.")
if 'elżbieta' not in favourite_languages:
    print("Elżbieta, weź udział w naszej ankiecie.")
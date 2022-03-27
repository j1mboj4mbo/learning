rzeki = {'Nil': 'Egipt', 'Wisła': 'Polska', 'Sekwana': 'Francja'}
for x in rzeki:
    print(f"{x} przepływa przez {rzeki[x]}")
print("\nLista rzek:")
for x in rzeki.keys():
    print(x)
print("\nLista państw:")
for x in rzeki.values():
    print(x)

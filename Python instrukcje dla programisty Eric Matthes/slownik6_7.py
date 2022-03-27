ob1 = {'first': 'Robert', 'last': 'Lewandowski', 'country': 'Poland'}
ob2 = {'first': 'Paul', 'last': 'Pogba', 'country': 'France'}
ob3 = {'first': 'Cristiano', 'last': 'Ronaldo', 'country': 'Portugal'}
people = [ob1, ob2, ob3]
for x in people:
    print(f"\nImię: {x['first']}\nNazwisko: {x['last']}\nKraj: {x['country']}")
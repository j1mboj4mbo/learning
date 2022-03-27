ob1 = {'country': 'spain', 'population': '1.62 mln', 'fact': 'older than city Rome'}
ob2 = {'country': 'italy', 'population': '2.87 mln', 'fact': 'has 280 fountains and more than 900 churches'}
ob3 = {'country': 'france', 'population': '2.16 mln', 'fact': "The Louvre is the world's largest art gallery and museum"}
cities = {'barcelona': ob1, 'rome': ob2, 'paris': ob3}
for i, y in cities.items():
    print(f"\nCity: {i.upper()}\nCountry: {y['country'].title()}\nPopulation: {y['population']}\nFact: {y['fact']}")
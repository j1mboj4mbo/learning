# Pracę rozpocznij od kopii programu user_profile.py utworzonego nieco wcześniej w tym rozdziale. Przygotuj własny
# profil przez wywołanie funkcji build_profile(), podaj imię, nazwisko oraz trzy inne pary klucz-wartość, które Cię
# opisują.
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einsten', location='princeton', field='fizyka')
user_profile1 = build_profile('artur', 'janduda', sex='male', age='21', additional_info='left-handed')
print(user_profile1)
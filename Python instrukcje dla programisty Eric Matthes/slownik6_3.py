slownik = {'if': 'jeżeli / warunkowanie (polecenie wykonuje się po spełnieniu warunku podanego po if)',
           'elif': 'jeżeli / warunkowanie po if (polecenie wykonuje się po spełnieniu warunku po elif, najpierw jest if, a później elif',
           'else': 'inaczej / żaden warunek nie został spełniony, wykonuje się wtedy polecenie po else',
           'pętla for x in y': 'wykonuje zapętlenie dla każdej pozycji x w y',
           '[]': 'pusta lista',
           '.keys': 'zwraca klucze w słowniku',
           '.values': 'zwraca wartości w słowniku',
           'set()/{}': 'zbiór, eliminuje duplikaty',
           'input': 'użytkownik sam wprowadza swoje dane / wymuszenie',
           'int(test)': 'zamiana liczby string na liczbe int'}
for x in slownik.keys():
    print(x)
for y in slownik.values():
    print(y)

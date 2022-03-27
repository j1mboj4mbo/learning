ob1 = ['adori gran', 'adori gran flam', 'adori vita vis']
ob2 = ['adura vita', 'adana ani', 'adevo mas grav vis']
ob3 = ['exura', 'exura gran', 'exura vita']
spells = {'attack runes': ob1, 'support runes': ob2, 'healing spells': ob3}
for i, x in spells.items():
    print(f"Spell type: {i}, pronounce: {x[0]}, {x[1]}, {x[2]}")
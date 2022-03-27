while(True):
    menu = input("Czy chcesz dodać uczestnika? T/N ").upper()
    if menu == "T":
        menuAge = int(input("Podaj wiek uczestnika: "))
        price = 0
        if menuAge <= 3:
            price = 0
            print(f"Koszt biletu wynosi {price}PLN.")
        elif 12 > menuAge > 3:
            price = 10
            print(f"Koszt biletu wynosi {price}PLN.")
        elif menuAge > 12:
            price = 15
            print(f"Koszt biletu wynosi {price}PLN.")
    elif menu == "N":
        break

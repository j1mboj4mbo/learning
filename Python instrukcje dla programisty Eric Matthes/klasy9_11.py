# Pracę rozpocznij od ćwiczenia 9.8. W jednym module umieść klasy User, Privileges i Admin. Przygotuj oddzielny plik,
# utwórz w nim egzemplarz klasy Admin i wywołaj metodę show_privileges(), aby sprawdzić, czy wszystko działa prawidłowo.
from klasy9_8 import Admin
user1 = Admin("Jimbo", "Jambo", 21, "Poland")
user1.privileges.show_privileges()


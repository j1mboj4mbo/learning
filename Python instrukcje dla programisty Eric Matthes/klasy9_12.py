# Klasę User umieść w jednym module, natomiast Privileges i Admin w oddzielnym. Następnie w innym pliku utwórz
# egzemplarz klasy Admin i wywołaj metodę show_privileges(), aby sprawdzić, czy wszystko działa prawidłowo.
import adminprivileges as ap

user1 = ap.Admin("J1MBO", "J4MBO", "21", "Poland")
user1.privileges.show_privileges()

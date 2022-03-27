# Zmodyfikuj funkcję make_shirt() tak, aby domyślnie były przygotowywane duże koszulki z nadrukowanym tekstem "Uwielbiam
# Pythona". Utwórz koszulki w rozmiarze dużym i średnim (obie z domyślnym tekstem) oraz koszulkę zw dowolnym rozmiarze i
# z innym tekstem nadrukowanym na niej.
def make_shirt(size="L", text="Uwielbiam Pythona"):
    print(f"Rozmiar koszulki {size}, tekst: {text}.")
make_shirt()
make_shirt(size="M")
make_shirt(size="S", text="supreme")

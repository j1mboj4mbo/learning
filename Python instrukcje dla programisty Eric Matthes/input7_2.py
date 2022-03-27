table = int(input("Ile osób chce zarezerwować stolik?: "))
if table > 8:
    print(f"Należy poczekać aż zwolni się stolik na {table} osób.")
else:
    print(f"Stolik na {table} osób jest gotowy do rezerwacji.")
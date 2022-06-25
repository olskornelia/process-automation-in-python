"""
Wymagania:
Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran.
"""
lista = []
while True:
    wartość = input("Podaj wartość, jeśli podasz słowo nie kończy się program:")
    if wartość == "nie":
        break
    lista.append(wartość)


print(lista)



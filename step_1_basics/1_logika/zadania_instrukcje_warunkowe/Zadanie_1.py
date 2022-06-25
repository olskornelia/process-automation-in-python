"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.

Pamiętaj o komentarzach.

Rezultat wypisz na ekran.

Podpowiedź:
Odpowiednio formatuj stringi
"""
x = int(input("Podaj liczbe "))
if x % 3 == 0:
    print(f'Liczba {x} jest podzielna przez 3')
elif x % 5 == 0:
    print(f'Liczba {x} jest podzielna przez 5')
elif x % 7 == 0:
    print(f'Liczba {x} jest podzielna przez 7')
else:
    print(f'Liczba nie jest podzielna przez 3, 5, 7')

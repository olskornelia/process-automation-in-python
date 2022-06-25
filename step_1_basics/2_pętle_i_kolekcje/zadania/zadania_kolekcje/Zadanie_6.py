"""
Stwórz listę trzech słowniki - Krystynę, Agnieszkę i Piotrka
Każdy kursant powinien mieć imię, informację o obecności i pracy domowej oraz punkty na egzaminie

Przejdź przez 6 dni kursu wypisując progres kursantów:
- Imię
- Obecność (ustaw losowo)
- Czy praca domowa jest odrobiona czy nie (ustaw losowo)
- Uzyskane punkty na egzaminie (ustaw losowo) (ustaw dopiero 6 dnia kursu)

Podpowiedź:
użyj random.choice do losowego ustawienia True i False
użyj random.randint do losowego ustawienia punktów (w zakresie 0 - 100)
"""
import copy pprint
from random import choice, randint

Krystyna = {'imię': 'Krystyna', 'obecność': None, 'praca domowa': None }
Agnieszka = {'imię': 'Agnieszka', 'obecność': None, 'praca domowa': None }
Piotrek = {'imię': 'Piotrek', 'obecność': None, 'praca domowa': None }

for day in range(1,7):
    for kursant in [Krystyna, Agnieszka, Piotrek]:
        k = copy.deepcopy(kursant)
        k['obecność'] = choice([True,False])
        k['praca domowa'] = choice([True,False])
        if day == 6:
            k['punkty'] = randint(0, 100)
        print(k)
        lista.append(k)


pprint(lista)

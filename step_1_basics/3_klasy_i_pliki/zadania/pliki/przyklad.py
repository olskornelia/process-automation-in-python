from faker import Faker
fake = Faker()

# with open("plik.txt", "w") as f: #w czysci plik w calosci i zapisuje dane
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)

with open("plik.txt", "a") as f: #otworzy plik i doda dane na samym koncu
     lines = '\n'.join([fake.text() for _ in range(100)])
     f.writelines(lines)
#
# with open("plik.txt", "r") as f: #otworzy plik i go odczyta
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)
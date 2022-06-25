lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
string = "Mój bardzo długi string wrzucę dodatkowo lorem ipsum" + lorem_ipsum

# wyciąganie liter poprzez indeks
print(string[2])

#od 8 do 12
print(string[8:12])

# od poczatku do 20 indexu
print(string[:20])

#wyciecie co 2 litere
print(string[:20:2])

# od 76 do konca
print(string[76:])

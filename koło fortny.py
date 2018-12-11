import random

# print("Plox użyj spacji na samym początku, bo jeszcze tego nie dokucowałem :D")
# print("Jeśli chcesz odgadywać hasło to zamiast literki wpisz: Odgaduję hasło")
# print("Ale dokładnie te słowa, te znaki o takim rozmiarze!")

with open("wiersz.txt") as data:
    hasla = [list(i.lower()) for i in data]
    for whitespace in range(len(hasla)):
        hasla[whitespace].remove("\n")
        space_found = True


def losowy(tab: list):
    return random.choice(tab)


def nagrody_los():
    pula = ["bankrut", 150, 200, 250, 500, 400, 300, 1500, 350]
    return random.choice(pula)


def podlogi(tab: list):
    przykryte = []
    for word in range(len(tab)):
        for letter in range(len(tab[word])):
            if tab[word][letter] != " ":
                przykryte.append("_")
            else:
                przykryte.append(" ")
    return przykryte


def zgadywanie(szukana, zakryta):
    pieniadze = 0
    flaga = False
    uzyte_litery = set()
    zbanowane = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]

    while not flaga:
        print("Masz obecnie", pieniadze, "złotych!")

        nagroda = nagrody_los()
        if nagroda == "bankrut":
            pieniadze = 0
            print("Straciłeś wszystkie pieniądze! :<")
            continue
        else:
            print("Możesz teraz wygrać aż", nagroda, "złotych!")

        print(*zakryta)
        literka = str(input("Podaj literkę: "))

        if len(uzyte_litery) == 23:
            literka = "Odgaduję hasło"

        if literka == "Odgaduję hasło":
            odpowiedz = input("podaj haslo: ")
            print("\n")
            if list(odpowiedz) == szukana:
                print("Zgadł(e)/(a)ś hasło! Brawo!")
                print("Wygrywasz:", pieniadze, "złotych!")
                break
            else:
                print("To nie jest poprawna odpowiedź.")

        if literka in uzyte_litery or literka in zbanowane or len(literka) != 1:
            print("Zbanowana / Już użyta!",)
            print("Użyte litery to:", sorted(uzyte_litery), "\n")
            continue

        uzyte_litery.add(literka)
        print("Użyte litery to:", sorted(uzyte_litery))
        znaleziona = False

        for znak in range(len(szukana)):
            if literka == szukana[znak]:
                znaleziona = True
                indeksy = [i for i, x in enumerate(szukana) if x == literka]
                for ind in indeksy:
                    zakryta[ind] = literka

        if znaleziona:
            print("Odgadł(e)/(a)ś literkę/i!", "\n")
            pieniadze += len(indeksy) * nagroda
        else:
            print("Nie znaleziono", "\n")

        if szukana == zakryta:
            print(zakryta)
            print("Zgadł(e)/(a)ś hasło! Brawo!")
            print("Wygrywasz:", pieniadze, "złotych!")
            flaga = True

    return "Gratulacje"


a = losowy(hasla)
b = podlogi(a)
c = zgadywanie(a, b)
print(c)

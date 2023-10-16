def print_bord():
    print(plaats[0], plaats[1], plaats[2])
    print(plaats[3], plaats[4], plaats[5])
    print(plaats[6], plaats[7], plaats[8])


def drieopeenrei(speler):
    if (plaats[0] == speler and plaats[1] == speler and plaats[2] == speler) or (
            plaats[3] == speler and plaats[4] == speler and plaats[5] == speler) or (
            plaats[6] == speler and plaats[7] == speler and plaats[8] == speler) or (
            plaats[0] == speler and plaats[3] == speler and plaats[6] == speler) or (
            plaats[1] == speler and plaats[4] == speler and plaats[7] == speler) or (
            plaats[2] == speler and plaats[5] == speler and plaats[8] == speler) or (
            plaats[0] == speler and plaats[4] == speler and plaats[8] == speler) or (
            plaats[2] == speler and plaats[4] == speler and plaats[6] == speler):
        return True


spelactief = True
while spelactief:
    print("Welkom bij Italiaanse Boter, Kaas en Eieren")
    naamSpeler1 = input("Wat is de naam van speler 1?")
    naamSpeler2 = input("Wat is de naam van speler 2?")
    plaats = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    plaatsen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_bord()
    for turn in range(3):
        while True:
            plaatsSpeler = input(f"Waar wil {naamSpeler1} een steen plaatsen?")
            if plaatsSpeler not in plaatsen:
                print("Antwoord met een plaats tussen de 1 en 9")
            elif plaatsSpeler in plaats:
                plaats[int(plaatsSpeler) - 1] = "X"
                print_bord()
                break
            else:
                print("Deze plaats is bezet")
            print_bord()
        while True:
            if drieopeenrei("X"):
                break
            plaatsSpeler = input(f"Waar wil {naamSpeler2} een steen plaatsen?")
            if plaatsSpeler not in plaatsen:
                print("Antwoord met een plaats tussen de 1 en 9")
            elif plaatsSpeler in plaats:
                plaats[int(plaatsSpeler) - 1] = "O"
                print_bord()
                break
            else:
                print("Deze plaats is bezet")
            print_bord()
    geenDrieOpEenRij = True
    while geenDrieOpEenRij:
        if drieopeenrei("X"):
            print(f"{naamSpeler1} heeft gewonnen")
            break
        if drieopeenrei("O"):
            print(f"{naamSpeler2} heeft gewonnen")
            break
        verplaatsjuist = False
        while not verplaatsjuist:
            verplaats = input(f"Welke steen wil {naamSpeler1} verplaatsen")
            if verplaats not in plaatsen:
                print("Antwoord met een plaats tussen de 1 en 9")
                print_bord()
            elif plaats[int(verplaats) - 1] != "X":
                print("Hier staat geen steen van jou")
                print_bord()
            else:
                print_bord()
                while True:
                    plaatsSpeler = input("Waar wil je deze steen plaatsen?")
                    if plaatsSpeler not in plaatsen:
                        print("Antwoord met een plaats tussen de 1 en 9")
                    elif plaatsSpeler in plaats:
                        plaats[int(verplaats) - 1] = verplaats
                        plaats[int(plaatsSpeler) - 1] = "X"
                        verplaatsjuist = True
                        print_bord()
                        break
                    else:
                        print("Deze plaats is bezet")
                    print_bord()
        if drieopeenrei("X"):
            print(f"{naamSpeler1} heeft gewonnen")
            break
        verplaatsjuist = False
        while not verplaatsjuist:
            verplaats = input(f"Welke steen wil {naamSpeler2} verplaatsen")
            if verplaats not in plaatsen:
                print("Antwoord met een plaats tussen de 1 en 9")
                print_bord()
            elif plaats[int(verplaats) - 1] != "O":
                print("Hier staat geen steen van jou")
                print_bord()
            else:
                print_bord()
                while True:
                    plaatsSpeler = input("Waar wil je deze steen plaatsen?")
                    if plaatsSpeler not in plaatsen:
                        print("Antwoord met een plaats tussen de 1 en 9")
                    elif plaatsSpeler in plaats:
                        plaats[int(verplaats) - 1] = verplaats
                        plaats[int(plaatsSpeler) - 1] = "O"
                        verplaatsjuist = True
                        print_bord()
                        break
                    else:
                        print("Deze plaats is bezet")
                    print_bord()
    antwoordjuist = False
    while not antwoordjuist:
        antwoord = input("Wil je nog een keer spelen?(ja/nee)")
        if antwoord.lower() == "ja":
            antwoordjuist = True
        elif antwoord.lower() == "nee":
            antwoordjuist = True
            print("Dankjewel voor het spelen van Italiaanse Boter, Kaas en Eieren")
            spelactief = False
